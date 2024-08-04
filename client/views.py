from django.shortcuts import render
from django.http import HttpResponse
from .createValidator import CreateValidator

def create(request):
    if request.method == "POST":
        #debug
        '''
        print(request.POST.get('name', False))
        print(request.POST.get('email', False))
        print(request.POST.get('password', False))
        '''
        
        validator = CreateValidator(request.POST['name'], request.POST['email'], request.POST['password'])
        context = {'validator':validator}
        
        if validator.invalidForm:
            return render(request, "client/create.html", context)
        else:
            return HttpResponse('Account created')
    else:
        return render(request, "client/create.html", {})


