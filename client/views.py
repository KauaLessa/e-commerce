from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.exceptions import TemplateDoesNotExist
from .formsValidators import CreateAccValidator
# from .formsValidators import SignInValidator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ManageLoginForm, ChangePasswordForm, ManageLocationForm, ManagePaymentForm, CommentForm
from django.urls import reverse
from django.core.exceptions import ViewDoesNotExist, FieldError
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Locations, PaymentMethod, Comments
from products.models import Product

def index(request):
    try:
        return render(request, "base.html", {})
    except ViewDoesNotExist as e:
        print(f"Can't load the requested view {e}")
        raise

def create(request):
    if request.method == "POST":
        #debug
        '''
        print(request.POST.get('name', False))
        print(request.POST.get('email', False))
        print(request.POST.get('password', False))
        '''

        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        validator = CreateAccValidator(name, email, password)
        
        if validator.validate_form():
            try:
                return render(request, "client/create.html", {'validator':validator})
            except TemplateDoesNotExist as e:
                print(f"Can't find requested template. {e}")
                raise
        else:
            new = User.objects.create(username=name, email=email)
            new.set_password(password)
            new.save()
            return HttpResponseRedirect(reverse('signIn'))
    else:
        try:
            return render(request, "client/create.html", {})
        except ViewDoesNotExist as e:
            print(f"Can't load the requested view {e}")
            raise

def signIn(request):
    if request.method == "POST":
        '''
        DEBUG
        print(request.POST.get('email', False))
        print(request.POST.get('password', False))
        '''
        
        name = request.POST['name']
        password = request.POST['password']
            
        user = authenticate(request, username=name, password=password)
        print(user)
        
        if not user:
            try:
                return render(request, "client/sign_in.html", {'error': 'Invalid name or password'})
            except TemplateDoesNotExist as e:
                print(f"Can't find the requested template. {e}")
                raise
        else:
            print(user)
            login(request, user)
            return HttpResponseRedirect(reverse('account'))
    else:

        try:
            return render(request, "client/sign_in.html", {})
        except TemplateDoesNotExist as e:
            print(f"Can't find the requested template. {e}")
            raise

@login_required
def account(request):
    try:
        location = Locations.objects.get(user=request.user)
    except Locations.DoesNotExist:
        location = None

    context = {
        'user': request.user,
        'location': location
    }

    try:
        return render(request, "client/accData.html", context)
    except ViewDoesNotExist as e:
        print(f"Can't load the requested view {e}")
        raise

@login_required(login_url='/signIn/')
def updateLogin(request):
    # user = request.user
    if request.method == "POST":

        form = ManageLoginForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            try:
                return HttpResponseRedirect(reverse('account'))
            except ViewDoesNotExist as e:
                print(f"Can't load requested view {e}")
                raise
        else:
            try:
                return render(request, 'client/userManagement.html', {'form' : form})
            except ViewDoesNotExist as e:
                print(f"Can't load requested view {e}")
                raise
    else: 
        form = ManageLoginForm(instance=request.user)
        try:
            return render(request, "client/userManagement.html", {'form' : form})
        except ViewDoesNotExist as e:
            print(f"Can't load the requested template. {e}")
            raise

@login_required
def manage_location(request):

    try:
        loc = Locations.objects.get(user=request.user)
    except Locations.DoesNotExist:
        loc = None

    if request.method == 'POST':
        form = ManageLocationForm(request.POST, instance=loc) if loc else ManageLocationForm(request.POST)

        if form.is_valid():
            new_loc = form.save(commit=False)
            new_loc.user=request.user
            new_loc.save()
            return HttpResponseRedirect(reverse('account'))
        else:
            return render(request, 'client/manage_location.html', {'form':form,'loc':loc})
    else:
        form = ManageLocationForm(instance=loc) if loc else ManageLocationForm()
        return render(request, 'client/manage_location.html', {'form':form, 'loc':loc})

@login_required
def manage_payment(request):

    try:
        payment_info = PaymentMethod.objects.get(user=request.user)
    except PaymentMethod.DoesNotExist:
        payment_info = None

    if request.method == 'POST':
        form = ManagePaymentForm(request.POST, instance=payment_info) if payment_info else ManagePaymentForm(request.POST)

        if form.is_valid():
            new_payment_info = form.save(commit=False)
            new_payment_info.user=request.user
            new_payment_info.save()
            return HttpResponseRedirect(reverse('account'))
        else:
            return render(request, 'client/manage_payment.html', {'form':form,'payment_info':payment_info})
    else:
        form = ManagePaymentForm(instance=payment_info) if payment_info else ManagePaymentForm()
        return render(request, 'client/manage_payment.html', {'form':form, 'payment_info':payment_info})

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('signIn')
    template_name = 'client/changePassword.html'

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('signIn'))

@login_required
def make_comment(request):

    product_id = request.GET.get('product-id')

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            if product_id:
                Comments.objects.create(
                    user = User.objects.get(id=request.user.id),
                    product = Product.objects.get(id=product_id),
                    user_comment = form.cleaned_data['comment']
                )
                return HttpResponseRedirect(reverse('product_page', args=[product_id]))
            else:
                Comments.objects.create(
                    user=User.objects.get(id=request.user.id),
                    user_comment=form.cleaned_data['comment']
                )
                return HttpResponseRedirect(reverse('contact_us'))
    else:
        form = CommentForm()
    try:
        return render(request, 'client/comments.html', {'form': form})
    except (TemplateDoesNotExist, ViewDoesNotExist) as e:
        print(e)
        raise

@login_required
def answer_comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            Comments.objects.filter(id=id).update(answer=form.cleaned_data['comment'])
            return HttpResponse('Answer send')
    else:
        form = CommentForm()

    return render(request, 'client/answer_comment.html', {'form': form})

def contact_us(request):
    comments = Comments.objects.filter(product__isnull=True)
    return render(request, 'client/contact_us.html', {'user':request.user, 'comments':comments})