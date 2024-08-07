from django.shortcuts import render
from django.http import HttpResponse
from .formsValidators import CreateAccValidator
from .formsValidators import SignInValidator
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "client/base.html", {})

def create(request):
    if request.method == "POST":
        #debug
        '''
        print(request.POST.get('name', False))
        print(request.POST.get('email', False))
        print(request.POST.get('password', False))
        '''
        
        validator = CreateAccValidator(request.POST['name'], request.POST['email'], request.POST['password'])
        context = {'validator':validator}
        
        if validator.invalidForm:
            return render(request, "client/create.html", context)
        else:
            return HttpResponse('Account created')
    else:
        return render(request, "client/create.html", {})
    
def signIn(request):
    if request.method == "POST":
        #debug
        '''
        print(request.POST.get('email', False))
        print(request.POST.get('password', False))
        '''
        
        validator = SignInValidator(request.POST['email'], request.POST['password'])
        context = {'validator':validator}
        
        if validator.invalidForm:
            return render(request, "client/sign_in.html", context)
        else:
            return HttpResponse('You are logged in')
    else:
        return render(request, "client/sign_in.html", {})
    
def account(request):
    return render(request, "client/accData.html", {})

def updateLogin(request):
    return render(request, "client/updateLogin.html", {})

