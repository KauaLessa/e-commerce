from ..models import Product, Cart, CartItem
from django.db.models import Sum

class Subject(Product):

    class Meta:
        proxy = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._observers = self.setObservers()

    def setObservers(self):
        cart_items = CartItem.objects.filter(product=self)
        return [Observer.objects.get(id=cart_item.cart.id) for cart_item in cart_items]

    def addObserver(self, obs_cart) -> bool:
        """obs_cart is an observer instance"""
        if obs_cart not in self._observers:
            self._observers.append(Observer.objects.get(id=obs_cart.id))
            return True
        return False

    def removeObserver(self, obs_cart) -> bool:
        """obs_cart is an observer instance"""
        try:
            self._observers.remove(obs_cart)
            return True
        except ValueError:
            return False

    def notifyObservers(self):
        for observer in self._observers:
            observer.update()

    def verifyState(self):
        product = Product.objects.get(id=self.pk)

        if self.discount_percent != product.discount_percent or self.price != product.price:
            Product.recalc_price(self)
            self.notifyObservers()

class Observer(Cart):

    class Meta:
        proxy = True

    def update(self):
        cart = Cart.objects.get(id=self.pk)
        total_cost = Cart.get_items(cart).aggregate(total=Sum('effective_price'))['total']

        # Atualiza o total no carrinho
        cart.total_cost = total_cost
        cart.save()
