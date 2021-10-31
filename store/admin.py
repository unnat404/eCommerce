from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(ShippingAddress)

# admin.site,register(User) 
# Note: User is Django's in-built model and so need not bne registered here seperately 
# to view the models in "Django admin" site 