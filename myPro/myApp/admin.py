from django.contrib import admin
from .models import User,Address,Product,OrderList,Cart,CartItem,OrderTracking
# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(OrderList)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderTracking)