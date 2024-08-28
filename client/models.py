from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Logins', models.DO_NOTHING, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    district = models.CharField(max_length=15, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
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
        
        