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
    review_product
from products.views import show_cart, remove_product_from_cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"), 
    path('create/', views.create, name="create"),
    path('signIn/', views.signIn, name="signIn"),
    path('account/', views.account, name="account"),
    path('updateLogin/', views.updateLogin, name="updateLogin"),
    path('changePassword/', login_required(ChangePasswordView.as_view(), login_url='/signIn/'), name="changePassword"),
    path('logout/', views.logout_user, name="logout"),
    path('get-product-id/', get_product_id, name="get_product_id"),
    path('add-product/', add_product, name="add_product"),
    path('manage-product/<int:id>/', manage_product, name="manage_product"),
    path('catalog/', catalog, name="catalog"),
    path('product/<int:id>/', product_page, name="product_page"),
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>', remove_product_from_cart, name="remove_product_from_cart"),
    path('cart/', show_cart, name='show_cart'),
    path('review-product/<int:product_id>/<str:username>/', review_product, name="review_product"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)