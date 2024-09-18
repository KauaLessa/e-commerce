from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
class CreateAccValidator:
    invalidNameMsg = '*Name: 3 characters min'
    invalidPasswordMsg = '*Password: 8 characters min'
    invalidEmailMsg = '*Email: Invalid email address'
    nameExistsMsg = '*Username already exists'

    def __init__(self, name: str, email: str, password: str):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__invalidName = False
        self.__invalidPassword = False
        self.__invalidEmail = False
        self.__nameExists = False
        self.__invalid = False

    @property
    def invalid(self):
        return self.__invalid

    @property
    def invalidName(self):
        return self.__invalidName

    @property
    def invalidEmail(self):
        return self.__invalidEmail

    @property
    def invalidPassword(self):
        return self.__invalidPassword

    @property
    def nameExists(self):
        return self.__nameExists

    def validate_atts_type(self) -> bool:
        atts = [self.__name, self.__email, self.__password]

        self.__invalid = not all(map(lambda x: isinstance(x, str), atts))

        return self.__invalid

    def validate_form(self) -> bool:
        """
        returns true if form is invalid
        """
        
        if self.validate_atts_type():
            return self.__invalid

        if len(self.__name) < 3:
            self.__invalidName = True

        if len(self.__password) < 8:
            self.__invalidPassword = True

        try:
            if User.objects.get(username=self.__name):
                self.__nameExists = True
        except User.DoesNotExist:
            pass
        try:
            validate_email(self.__email)
        except ValidationError:
            self.__invalidEmail = True

        self.__invalid = self.__invalidName or self.__nameExists or self.__invalidPassword or self.__invalidEmail
        return self.__invalid