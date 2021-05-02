from django import forms

from .models import Pizza, Toppings


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["name"]
        labels = {"name": ""}
