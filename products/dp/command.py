from abc import ABC, abstractmethod
from products.models import Cart, Product, OrderItem
from django.db.models import F, When, Case

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class OrderFromCart(Command):
    def __init__(self, cart):
        self._cart = cart

    def execute(self):
        Cart.place_order_from_cart(self._cart)
        Cart.remove_all_items(self._cart)

class MakeOrder(Command):
    def __init__(self, user, product_id):
        self._product_id = product_id
        self._user = user

    def execute(self):
        pd = Product.objects.filter(id=self._product_id).annotate(
            effective_price=Case(
                When(sale_price__isnull=False, then=F('sale_price')),
                default=F('price')
            )
        ).first()

        OrderItem.objects.create(product=pd, user=self._user, quantity=1, cost=pd.effective_price)

class AddToCartCommand(Command):
    def __init__(self, cart, cart_item):
        self._cart = cart
        self._cart_item = cart_item

    def execute(self):
        # Atualizando campos
        self._cart_item.quantity += 1
        self._cart.total_items += 1

        product = self._cart_item.product

        if product.sale_price:

            # DEBUG
            # print("Calculating total price...")
            # print(f"{self._cart.total_cost} + {product.sale_price} = {self._cart.total_cost + product.sale_price}")

            self._cart.total_cost += product.sale_price
        else:
            self._cart.total_cost += product.price

        self._cart_item.save()
        self._cart.save()

class RemoveProductCommand(Command):
    def __init__(self, cart, cart_item):
        self._cart = cart
        self._cart_item = cart_item

    def execute(self):
        if self._cart_item.product.sale_price:
            self._cart.total_cost -= self._cart_item.quantity * self._cart_item.product.sale_price
        else:
            self._cart.total_cost -= self._cart_item.quantity * self._cart_item.product.price

        self._cart.total_items -= self._cart_item.quantity
        self._cart_item.delete()
        self._cart.save()

class Invoker:
    def __init__(self, command: Command):
        self._command = command

    def setCommand(self, command: Command):
        self._command = command

    def executeCommand(self):
        self._command.execute()