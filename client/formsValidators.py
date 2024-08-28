from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Logins

class CreateAccValidator():
    invalidNameMsg = '*Name: 3 characters min' 
    invalidPasswordMsg = '*Password: 8 characters min'
    invalidEmailMsg = '*Email: Invalid email address'
    emailExistsMsg = '*Email: Email alredy exists'
     
    def __init__(self, name:str, email:str, password:str):

        # Tratamento de erro

        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        
        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        if not isinstance(password, str):
            raise TypeError("Password must be a string")

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
        

'''

class SignInValidator():
    invalidMsg = "Wrong email or password."
     
    def __init__(self, email:str, password:str):

        # tratamento de erro 
        # checando se argumentos sao do tipo esperado

        if not isinstance(email, str):
            raise TypeError('Email must be a string')

        if not isinstance(password, str):
            raise TypeError('Password must be a string')


        self.invalidForm = False

        # tratamento de erro

        try:
            if Logins.objects.get(email=email, password=password):
                pass
        except Logins.DoesNotExist:
            self.invalidForm = True

'''


'''

class UpdateAccValidator():
    invalidNameMsg = '*Name: 3 characters min' 
    invalidPasswordMsg = '*Password: 8 characters min'
    invalidEmailMsg = '*Email: Invalid email address'
     
    def __init__(self, name:str, email:str, password:str):

        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        
        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        if not isinstance(password, str):
            raise TypeError("Password must be a string")

        self.invalidName = False
        self.invalidPassword = False
        self.invalidEmail = False
        self.invalidForm = False
        
        if name and len(name) < 3:
            self.invalidName = True   
            
        if password and len(password) < 8:
            self.invalidPassword = True
            
        if email:
            try:
                validate_email(email)
            except ValidationError:
                self.invalidEmail = True
 
        self.invalidForm = self.invalidName or self.invalidPassword or self.invalidEmail
        # Debug print(self.invalidForm) 

'''
        