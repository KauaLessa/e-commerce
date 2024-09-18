"""
URL configuration for e_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from client import views
from client.views import ChangePasswordView
from django.contrib.auth.decorators import login_required
from products.views import add_product, get_product_id, manage_product, catalog, product_page, add_to_cart, \
    review_product, get_department, set_department_discount, show_cart, remove_product_from_cart, \
    make_order, make_order_from_cart, show_orders, remove_order
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"), 
    path('create/', views.create, name="create"),
    path('signIn/', views.signIn, name="signIn"),
    path('account/', views.account, name="account"),
    path('updateLogin/', views.updateLogin, name="updateLogin"),
    path('changePassword/', login_required(ChangePasswordView.as_view(), login_url='/signIn/'), name="changePassword"),
    path('manage-location/', views.manage_location, name="manage_location"),
    path('manage-payment/', views.manage_payment, name="manage_payment"),
    path('logout/', views.logout_user, name="logout"),
    path('make-comment/', views.make_comment, name="make_comment"),
    path('answer-comment/<int:id>/', views.answer_comment, name="answer_comment"),
    path('contact-us/', views.contact_us, name="contact_us"),
    path('get-product-id/', get_product_id, name="get_product_id"),
    path('add-product/', add_product, name="add_product"),
    path('manage-product/<int:id>/', manage_product, name="manage_product"),
    path('catalog/', catalog, name="catalog"),
    path('product/<int:id>/', product_page, name="product_page"),
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>', remove_product_from_cart, name="remove_product_from_cart"),
    path('cart/', show_cart, name='show_cart'),
    path('review-product/<int:product_id>/<str:username>/', review_product, name="review_product"),
    path('get-department/', get_department, name="get_department"),
    path('set-department-discount/<str:department>', set_department_discount, name="set_department_discount"),
    path('admin/', admin.site.urls),
    path('make-order/<int:id>/', make_order, name="make_order"),
    path('make-order-from-cart/', make_order_from_cart, name='make_order_from_cart'),
    path('orders/', show_orders, name="orders"),
    path('remove-order<int:id>/', remove_order, name="remove_order")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)