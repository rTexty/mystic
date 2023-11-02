from django.contrib import admin

# Register your models here.

from Cars.models import Car, Category, Brand

admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Brand)