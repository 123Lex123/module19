from django.urls import path
from .views import main_page, shop_page, cart_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('shop/', shop_page, name='shop_page'),
    path('cart/', cart_page, name='cart_page'),
]
