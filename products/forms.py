import django.forms as forms
from django.forms import models
from products.models import Product, Department
from django.core.validators import MinValueValidator, MaxValueValidator

class GetProductIdForm(forms.Form):
    template_name = 'client/acc_management.html'

    id = forms.IntegerField(label='ID')

class ProductForm(forms.ModelForm):
    template_name = 'client/acc_management.html'
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Select a department')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'discount_percent', 'department']

class ProductReviewForm(forms.Form):
    template_name = 'client/acc_management.html'

    rating = forms.IntegerField(
        validators = [
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    review = forms.CharField(widget=forms.Textarea)

class GetDepartmentForm(forms.Form):
    template_name = 'client/acc_management.html'
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label='Select a department')

class SetDepartmentDiscountForm(models.ModelForm):
    template_name = 'client/acc_management.html'

    class Meta:
        model = Department
        fields = ['discount_percent']



