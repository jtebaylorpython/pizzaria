from django.contrib import admin

from pizzas.models import Pizza, Toppings

admin.site.register(Pizza)
admin.site.register(Toppings)
