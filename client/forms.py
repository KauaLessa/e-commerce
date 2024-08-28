from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput, EmailField, EmailInput, PasswordInput
from django.core.validators import MinLengthValidator
from django.contrib.auth.forms import PasswordChangeForm

class ManageLoginForm(ModelForm):
    template_name = "client/acc_management.html"

    username = CharField(
        validators=[MinLengthValidator(3)],
        required = True,
        widget=TextInput(attrs={'placeholder': 'name'})
    )
    email = EmailField(
        required = True,
        widget=EmailInput(attrs={'placeholder': 'email'})
    )

    class Meta:
        model = User
        fields = ["username", "email"]

class ChangePasswordForm(PasswordChangeForm):
    template_name = "client/acc_management.html"