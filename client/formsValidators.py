from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Logins
from .client import User

class CreateAccValidator():
    invalidNameMsg = '*Name: 3 characters min' 
    invalidPasswordMsg = '*Password: 8 characters min'
    invalidEmailMsg = '*Email: Invalid email address'
    emailExistsMsg = '*Email: Email alredy exists'
     
    def __init__(self, name:str, email:str, password:str):
        self.invalidName = False
        self.invalidPassword = False
        self.emailExists = False
        self.invalidEmail = False
        self.invalidForm = False
        
        if len(name) < 3:
            self.invalidName = True   
            
        if len(password) < 8:
            self.invalidPassword = True
            
        try:
            if Logins.objects.get(email=email):
                self.emailExists = True
        except Logins.DoesNotExist:
            pass
            
        try:
            validate_email(email)
        except ValidationError:
            self.invalidEmail = True
 
        self.invalidForm = self.invalidName or self.invalidPassword or self.invalidEmail or self.emailExists
        # Debug print(self.invalidForm)         
        
class SignInValidator():
    invalidMsg = "Wrong email or password."
     
    def __init__(self, email:str, password:str):
        self.invalidForm = False

        try:
            if Logins.objects.get(email=email, password=password):
                pass
        except Logins.DoesNotExist:
            self.invalidForm = True