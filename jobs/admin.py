from django.contrib import admin
from .models import Product, Order, Stock, Engineer, Appointment

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Stock)
admin.site.register(Engineer)
admin.site.register(Appointment)
