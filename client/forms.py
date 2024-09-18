from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput, EmailField, EmailInput, PasswordInput
from django import forms
from django.core.validators import MinLengthValidator
from django.contrib.auth.forms import PasswordChangeForm
from client.models import Locations, PaymentMethod, Comments

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

class ManageLocationForm(ModelForm):
    template_name = "client/acc_management.html"

    class Meta:
        model = Locations
        exclude = ['user', 'id']

class ManagePaymentForm(ModelForm):
    template_name = "client/acc_management.html"

    expiration_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = PaymentMethod
        exclude = ['user', 'id']

class CommentForm(forms.Form):
    template_name = "client/acc_management.html"
    comment = forms.CharField(widget=forms.Textarea)
