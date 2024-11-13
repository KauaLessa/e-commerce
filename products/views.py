from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SubjectProductForm, GetProductIdForm, ProductReviewForm, GetDepartmentForm, \
    SetDepartmentDiscountForm, ProductForm
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem, Cart, ProductReview, Department, OrderItem
from django.contrib.auth.models import User
from django.template.exceptions import TemplateDoesNotExist
from django.core.exceptions import ViewDoesNotExist, ObjectDoesNotExist, FieldDoesNotExist
from django.urls.exceptions import NoReverseMatch
from django.urls import reverse
from django.db.models.functions import Coalesce
from client.models import Comments
from .dp.observer import Subject
from .dp import command as cmd
from .dp import cor
from .dp.facade import CompleteHandlerChain

@login_required(login_url='/signIn/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            pd = form.save(commit=False)
            Product.recalc_price(pd)
            pd.save()
            form = ProductForm()
        try:
            return render(request, 'products/add_product.html', {'form': form})
        except (TemplateDoesNotExist, ViewDoesNotExist) as e:
            print(e)
            raise
    else:
        form = ProductForm()
        try:
            return render(request, 'products/add_product.html', {'form': form})
        except (TemplateDoesNotExist, ViewDoesNotExist) as e:
            print(e)
            raise

@login_required(login_url='/signIn/')
def get_product_id(request):
    if request.method == 'POST':
        form = GetProductIdForm(request.POST)

        if form.is_valid():
            id = form.cleaned_data['id']
            try:
                return HttpResponseRedirect(reverse('manage_product', args=[id]))
            except NoReverseMatch as e:
                print(f"Could not find reverse match. {e}")
                raise
        else:
            try:
                return render(request, 'products/get_product_id.html', {'form': form})
            except (TemplateDoesNotExist, ViewDoesNotExist) as e:
                print(e)
                raise
    else:
        form = GetProductIdForm()

        try:
            return render(request, 'products/get_product_id.html', {'form':form})
        except (TemplateDoesNotExist, ViewDoesNotExist) as e:
            print(e)
            raise

@login_required()
def manage_product(request, id):

    try:
        product_subject = Subject.objects.get(id=id)
    except (FieldDoesNotExist, ObjectDoesNotExist) as e:
        print(e)
        raise

    if request.method == 'POST':
        form = SubjectProductForm(request.POST, request.FILES, instance=product_subject)

        if form.is_valid():
            product_new = form.save(commit=False)
            product_new.verifyState()
            product_new.save()

            try:
                return HttpResponseRedirect(reverse('get_product_id'))
            except NoReverseMatch as e:
                print(f'Could not find reverse match. {e}')
                raise
        else:
            try:
                return render(request, 'products/manage_product.html', {'form': form})
            except (TemplateDoesNotExist, ViewDoesNotExist) as e:
                print(e)
                raise
    else:
        form = SubjectProductForm(instance=product_subject)
        try:
            return render(request, 'products/manage_product.html', {'form':form})
        except (TemplateDoesNotExist, ViewDoesNotExist) as e:
            print(e)
            raise

@login_required
def show_cart(request):
    try:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except FieldDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

    context =  {'cart':cart, 'cart_items':cart_items}

    try:
        return render(request, 'products/cart.html', context)
    except TemplateDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

@login_required
def make_order_from_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    if cart:
        chain = CompleteHandlerChain()
        return chain.handle(request)
    else:
        return HttpResponseRedirect(reverse('show_cart'))

@login_required
def add_to_cart(request, id):
    try:
        pd = Product.objects.get(id=id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(product=pd, cart=cart)
    except FieldDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

    invoker = cmd.Invoker(cmd.AddToCartCommand(cart, cart_item))
    invoker.executeCommand()

    try:
        return HttpResponseRedirect(reverse('show_cart'))
    except (NoReverseMatch, ViewDoesNotExist) as e:
        print(e)
        raise

@login_required
def remove_product_from_cart(request, id):

    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(id=id)

    except FieldDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

    invoker = cmd.Invoker(cmd.RemoveProductCommand(cart, cart_item))
    invoker.executeCommand()

    # redirecionar para carrinho do usuario

    try:
        return HttpResponseRedirect(reverse('show_cart'))
    except (NoReverseMatch, ViewDoesNotExist) as e:
        print(e)
        raise

def catalog(request):

    department = request.GET.get('department')
    sort_by = request.GET.get('sort_by')
    products = Product.objects.all()

    print(f"Printing department: {department}")

    # Sorting..
    if department and department != 'None':
        dp = Department.objects.get(dp=department)
        print(f'Printing department query {dp}')
        products = products.filter(department=dp)

    if products:
        if sort_by == 'low_to_high':
            products = products.annotate(
                effective_price=Coalesce('sale_price', 'price')) \
                .order_by('effective_price')

        elif sort_by == 'high_to_low':
            products = products.annotate(
                effective_price=Coalesce('sale_price', 'price')) \
                .order_by('-effective_price')

    context = {
        'products': products,
        'department': department,
        'sort_by': sort_by,
    }

    try:
        return render(request, 'products/catalog.html', context)
    except (TemplateDoesNotExist, ViewDoesNotExist) as e:
        print(e)
        raise

def product_page(request, id):

    try:
        product = Product.objects.get(id=id)
        reviews = ProductReview.objects.filter(product=product)
        questions = Comments.objects.filter(product=product)
    except FieldDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

    context = {
        'product':product,
        'reviews':reviews,
        'user':request.user,
        'questions':questions
    }

    try:
        return render(request, 'products/product.html', context)
    except (TemplateDoesNotExist, ViewDoesNotExist) as e:
        print(e)
        raise

@login_required
def review_product(request, product_id, username):
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)

        if form.is_valid():
            try:
                ProductReview.objects.create(
                    user = User.objects.get(username=username),
                    product = Product.objects.get(id=product_id),
                    rating = form.cleaned_data['rating'],
                    review = form.cleaned_data['review']
                )
            except FieldDoesNotExist as e:
                print(f"The requested field does not exist. {e}")
            try:
                return HttpResponseRedirect(reverse('product_page', args=[product_id]))
            except NoReverseMatch as e:
                print(f'Could not find reverse match. {e}')
                raise
        else:
            try:
                return render(request, 'products/review_product.html', {'form':form})
            except (TemplateDoesNotExist, ViewDoesNotExist) as e:
                print(f'Error rendering page. {e}')
                raise
    else:
        form = ProductReviewForm()

        try:
            return render(request, 'products/review_product.html', {'form': form})
        except (TemplateDoesNotExist, ViewDoesNotExist) as e:
            print(f'Error rendering page. {e}')
            raise

@login_required
def get_department(request):

    if request.method == 'POST':
        form = GetDepartmentForm(request.POST)

        if form.is_valid():
            department = form.cleaned_data['department']
            return HttpResponseRedirect(reverse('set_department_discount', args=[department]))
        else:
            return render(request, 'products/get_department.html', {'form':form})
    else:
        form = GetDepartmentForm()
        return render(request, 'products/get_department.html', {'form':form})

@login_required
def set_department_discount(request, department):
    dp = Department.objects.get(dp=department)
    dp_old_discount_percent = dp.discount_percent

    if request.method == 'POST':
        form = SetDepartmentDiscountForm(request.POST, instance=dp)

        if form.is_valid():
            dp = form.save()
            dp_products = Product.objects.filter(department=dp)

            if dp.discount_percent != dp_old_discount_percent:

                for product in dp_products:
                    Product.recalc_price(product)
                    Cart.recalc_price(product)

            return HttpResponseRedirect(reverse('get_department'))
        else:
            return render(request, 'products/set_department_discount.html', {'form':form})
    else:
        form = SetDepartmentDiscountForm(instance=dp)
        return render(request, 'products/set_department_discount.html', {'form':form})

def make_order(request, id):
    if request.user.is_authenticated:

        location_handler = cor.LocationHandler()
        payment_handler = cor.PaymentInfoHandler()
        location_handler.set_next(payment_handler)
        response = location_handler.handle(request)

        if not response:
            invoker = cmd.Invoker(cmd.MakeOrder(request.user, id))
            invoker.executeCommand()
            return HttpResponseRedirect(reverse('orders'))

        return response

    return HttpResponse('Order placed successfully')

@login_required
def show_orders(request):
    orders = OrderItem.objects.filter(user=request.user)
    return render(request, 'products/orders.html', {'orders':orders})

@login_required
def remove_order(request, id):
    OrderItem.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('orders'))