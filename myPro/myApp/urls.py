from django.urls import path
from .import views
urlpatterns = [

    path('User/',views.User),
    path('Address/',views.Address),
    path('Product/',views.Product),
    path('OrderList/',views.OrderList),
    path('Cart/',views.Cart),
    path('delete_cart/<int:cart_id>/',views.delete_cart),
    path('CartItem/',views.CartItem),
    path('OderTracking/',views.OrderTracking)
]