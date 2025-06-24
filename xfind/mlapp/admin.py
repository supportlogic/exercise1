from django.contrib import admin

from .models import Customer, DataSource, Item

admin.site.register(Customer)
admin.site.register(DataSource)
admin.site.register(Item)