from products.dp import cor

class CompleteHandlerChain:
    def __init__(self):
        # Configurando a cadeia de handlers
        self._logged_in_handler = cor.LoggedInHandler()
        self._cart_not_empty_handler = cor.CartStateHandler()
        self._payment_info_handler = cor.PaymentInfoHandler()
        self._location_handler = cor.LocationHandler()
        self._place_order_handler = cor.CartPlaceOrderHandler()
        self._setChain()

    def _setChain(self):
        # Ligando os handlers na cadeia
        self._logged_in_handler.set_next(self._cart_not_empty_handler) \
            .set_next(self._payment_info_handler) \
            .set_next(self._location_handler) \
            .set_next(self._place_order_handler)

    def handle(self, request):
        return self._logged_in_handler.handle(request)