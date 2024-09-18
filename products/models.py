from bdb import effective

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import F, Sum, Case, When

class Department(models.Model):
    dp = models.CharField(max_length=100)
    discount_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return self.dp

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    sale_price = models.DecimalField(null=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='media/')
    department = models.ForeignKey(Department,blank=True, null=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)
    discount_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return self.name

    @staticmethod
    def recalc_price(product):
        # recalcula o desconto

        if product.department:
            dp_discount = product.department.discount_percent
        else:
            dp_discount = 0

        product.sale_price = round(
            product.price * ((100 - dp_discount) / 100) * \
            ((100 - product.discount_percent) / 100), 2
        )

        if product.sale_price == product.price:
            product.sale_price = None

        print(product.sale_price)
        product.save()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    @staticmethod
    def get_items(cart):
        return CartItem.objects.filter(cart=cart).annotate(
            effective_price=Case(
                When(product__sale_price__isnull=False, then=F('quantity') * F('product__sale_price')),
                default=F('quantity') * F('product__price'),
            )
        )

    @staticmethod
    def recalc_price(product):
        pd_cart_items = CartItem.objects.filter(product=product)

        for pd_cart_item in pd_cart_items:
            cart = pd_cart_item.cart  # Instância do carrinho

            total_cost = Cart.get_items(cart).aggregate(total=Sum('effective_price'))['total']

            # Atualiza o total no carrinho
            cart.total_cost = total_cost
            cart.save()

    @staticmethod
    def place_order_from_cart(cart):
        cart_items = Cart.get_items(cart)

        order_items = []

        for cart_item in cart_items:
            order_item = OrderItem(
                product=cart_item.product,
                quantity=cart_item.quantity,
                user=cart.user,
                cost=cart_item.effective_price
            )
            order_items.append(order_item)

        OrderItem.objects.bulk_create(order_items)

    @staticmethod
    def remove_all_items(cart):
        CartItem.objects.filter(cart=cart).delete()
        cart.total_cost = 0
        cart.total_items = 0
        cart.save()

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField()

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)