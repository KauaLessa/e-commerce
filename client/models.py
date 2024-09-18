from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Locations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)

    class Meta:
        managed = True
        db_table = 'locations'

class Logins(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    admin = models.IntegerField()
    creation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'logins'
        
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    cardholder_name = models.CharField(max_length=100)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)

class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_comment = models.TextField()
    answer = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

        
        