from django.shortcuts import redirect, get_object_or_404
from abc import ABC, abstractmethod
from products.models import Cart
from client.models import PaymentMethod, Locations
from products.dp.command import OrderFromCart, Invoker

class Handler(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class LoggedInHandler(Handler):
    def handle(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')
        return super().handle(request)

class CartStateHandler(Handler):
    def handle(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        if cart.total_items == 0:
            return redirect('show_cart')
        return super().handle(request)

class PaymentInfoHandler(Handler):
    def handle(self, request):
        try:
            PaymentMethod.objects.get(user=request.user)
        except PaymentMethod.DoesNotExist:
            return redirect('manage_payment')
        return super().handle(request)

class LocationHandler(Handler):
    def handle(self, request):
        try:
            Locations.objects.get(user=request.user)
        except Locations.DoesNotExist:
            return redirect('manage_location')
        return super().handle(request)

class CartPlaceOrderHandler(Handler):
    def handle(self, request):
        cart = Cart.objects.get(user=request.user)
        invoker = Invoker(OrderFromCart(cart))
        invoker.executeCommand()
        return redirect('orders')
