from django.contrib import admin
from .models.product import Product
from .models.order import Order
from .models.customer import Customer
from .models.contact import Contact
from .models import Carousel

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Carousel)