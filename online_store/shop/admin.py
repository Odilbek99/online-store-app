from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, About, Category, Product, Order, OrderDetail

admin.site.register(User)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)

