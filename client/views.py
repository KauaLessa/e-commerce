from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.exceptions import TemplateDoesNotExist
from .formsValidators import CreateAccValidator
# from .formsValidators import SignInValidator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ManageLoginForm, ChangePasswordForm
from django.urls import reverse
from django.core.exceptions import ViewDoesNotExist, FieldError
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

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
        context = {'validator':validator}
        
        if validator.invalidForm:
            try:
                return render(request, "client/create.html", context)
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

@login_required(login_url='/signIn/')    
def account(request):
    try:
        return render(request, "client/accData.html", {'user': request.user})
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

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('signIn')
    template_name = 'client/changePassword.html'

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('signIn'))