import django.forms as forms
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

class GetProductIdForm(forms.Form):
    template_name = 'client/acc_management.html'

    id = forms.IntegerField(label='ID')

class ProductForm(forms.ModelForm):
    template_name = 'client/acc_management.html'

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class ProductReviewForm(forms.Form):
    template_name = 'client/acc_management.html'

    rating = forms.IntegerField(
        validators = [
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    review = forms.CharField(widget=forms.Textarea)

