import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzaria.settings")

import django

django.setup()

from pizzas.models import Toppings

toppings = Toppings.objects.all()

for topping in toppings:
    print(topping.id, topping)

t = Toppings.objects.get(id=1)
print(t.text)
print(t.date_added)

entries = t.entry_set.all()
for entry in entries:
    print(entry)
