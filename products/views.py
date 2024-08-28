from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProductForm, GetProductIdForm, ProductReviewForm
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem, Cart, ProductReview
from django.contrib.auth.models import User
from django.template.exceptions import TemplateDoesNotExist
from django.core.exceptions import ViewDoesNotExist, ObjectDoesNotExist, FieldDoesNotExist
from django.urls.exceptions import NoReverseMatch
from django.urls import reverse

@login_required(login_url='/signIn/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = ProductForm()
        try:
            return render(request, 'products2/add_product.html', {'form': form})
        except TemplateDoesNotExist as e:
            print(f"Requested template does not exist. {e}")
            raise
        except ViewDoesNotExist as e:
            print(f"Requested view does not exist. {e}")
            raise
    else:
        form = ProductForm()
        try:
            return render(request, 'products2/add_product.html', {'form': form})
        except TemplateDoesNotExist as e:
            print(f"Requested template does not exist. {e}")
            raise
        except ViewDoesNotExist as e:
            print(f"Requested view does not exist. {e}")
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
            except TemplateDoesNotExist as e:
                print(f"Requested template does not exist. {e}")
                raise
            except ViewDoesNotExist as e:
                print(f"Requested view does not exist. {e}")
        else:
            try:
                return render(request, 'products2/get_product_id.html', {'form': form})
            except TemplateDoesNotExist as e:
                print(f"Requested template does not exist. {e}")
                raise
            except ViewDoesNotExist as e:
                print(f"Requested view does not exist. {e}")
                raise
    else:
        form = GetProductIdForm()

        try:
            return render(request, 'products2/get_product_id.html', {'form':form})
        except TemplateDoesNotExist as e:
            print(f"Requested template does not exist. {e}")
            raise
        except ViewDoesNotExist as e:
            print(f"Requested view does not exist. {e}")
            raise

@login_required(login_url='/signIn/')
def manage_product(request, id):
    try:
        pd = Product.objects.get(id=id)
    except FieldDoesNotExist as e:
        print(f'Requested model field does not exist. {e}')
        raise
    except ObjectDoesNotExist as e:
        print(f"The requested object does not exist. {e}")
        raise
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=pd)

        if form.is_valid():
            form.save()
            try:
                return HttpResponseRedirect(reverse('get_product_id'))
            except NoReverseMatch as e:
                print('Could not find reverse match. {e}')
                raise
            except TemplateDoesNotExist as e:
                print(f"Requested template does not exist. {e}")
                raise
            except ViewDoesNotExist as e:
                print(f"The requested view does not exist. {e}")
                raise
        else:
            try:
                return render(request, 'products2/manage_product.html', {'form': form})
            except TemplateDoesNotExist as e:
                print(f"Requested template does not exist. {e}")
                raise
            except ViewDoesNotExist as e:
                print(f"The requested view does not exist. {e}")
                raise
    else:
        form = ProductForm(instance=pd)
        try:
            return render(request, 'products2/manage_product.html', {'form':form})
        except TemplateDoesNotExist as e:
            print(f"Requested template does not exist. {e}")
            raise
        except ViewDoesNotExist as e:
            print(f"The requested view does not exist. {e}")
            raise

@login_required
def show_cart(request):
    try:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except FieldDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise
    except ObjectDoesNotExist as e:
        print(f"The requested object does not exist. {e}")
        raise

    context =  {'cart':cart, 'cart_items':cart_items}

    try:
        return render(request, 'products2/cart.html', context)
    except TemplateDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

    except ViewDoesNotExist as e:
        print(f"The requested view does not exist. {e}")
        raise

@login_required
def add_to_cart(request, id):
    # Pegando ou criando produto, item de carrinho e carrinho

    try:
        pd = Product.objects.get(id=id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(product=pd, cart=cart)
    except FieldDoesNotExist as e:
        print(f"The requested field does not exist")
        raise

    except ObjectDoesNotExist as e:
        print(f"The requested object does not exist. {e}")
        raise

    # Atualizando campos
    cart_item.quantity += 1
    cart.total_items += 1
    cart.total_cost += pd.price
    cart_item.save()
    cart.save()

    try:
        return HttpResponseRedirect(reverse('show_cart'))
    except NoReverseMatch as e:
        print('Could not find reverse match. {e}')
        raise

    except TemplateDoesNotExist as e:
        print(f"Requested template does not exist. {e}")
        raise

    except ViewDoesNotExist as e:
        print(f"The requested view does not exist. {e}")
        raise

@login_required
def remove_product_from_cart(request, id):

    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(id=id)
    except FieldDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

    cart.total_cost -= cart_item.quantity * cart_item.product.price
    cart.total_items -= cart_item.quantity
    cart_item.delete()
    cart.save()

    # redirecionar para carrinho do usuario

    try:
        return HttpResponseRedirect(reverse('show_cart'))
    except NoReverseMatch as e:
        print('Could not find reverse match. {e}')
        raise

    except TemplateDoesNotExist as e:
        print(f"Requested template does not exist. {e}")
        raise

    except ViewDoesNotExist as e:
        print(f"The requested view does not exist. {e}")
        raise

def catalog(request):
    products = Product.objects.all()

    try:
        return render(request, 'products2/catalog.html', {'products': products})
    except TemplateDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

    except ViewDoesNotExist as e:
        print(f"The requested view does not exist. {e}")
        raise

def product_page(request, id):

    try:
        product = Product.objects.get(id=id)
        reviews = ProductReview.objects.filter(product=product)
    except FieldDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

    context = {'product':product, 'reviews':reviews, 'user':request.user}

    try:
        return render(request, 'products2/product.html', context)
    except TemplateDoesNotExist as e:
        print(f"The requested field does not exist. {e}")
        raise

    except ViewDoesNotExist as e:
        print(f"The requested view does not exist. {e}")
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
                raise
            except ObjectDoesNotExist as e:
                print(f"Object does not exist. {e}")
                raise
            try:
                return HttpResponseRedirect(reverse('product_page', args=[product_id]))
            except NoReverseMatch as e:
                print('Could not find reverse match. {e}')
                raise
            except TemplateDoesNotExist as e:
                print(f"Requested template does not exist. {e}")
                raise
            except ViewDoesNotExist as e:
                print(f"The requested view does not exist. {e}")
        else:
            try:
                return render(request, 'products2/review_product.html', {'form':form})
            except TemplateDoesNotExist as e:
                print(f"The requested field does not exist. {e}")
                raise
            except ViewDoesNotExist as e:
                print(f"The requested view does not exist. {e}")
    else:
        form = ProductReviewForm()

        try:
            return render(request, 'products2/review_product.html', {'form': form})
        except TemplateDoesNotExist as e:
            print(f"The requested field does not exist. {e}")
            raise
        except ViewDoesNotExist as e:
            print(f"The requested view does not exist. {e}")
            raise