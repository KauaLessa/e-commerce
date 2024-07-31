from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(unique=True, max_length=50)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(
        blank=True,
        null=True,max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0),MaxValueValidator(1)]
    )
    insertion_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products'
