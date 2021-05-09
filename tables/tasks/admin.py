from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Table)
admin.site.register(Restaurant)
admin.site.register(Bar)
admin.site.register(Basket)
admin.site.register(Product)
