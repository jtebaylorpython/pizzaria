from django.shortcuts import render, redirect
from .models import Pizza, Toppings
from .forms import PizzaForm


def index(request):
    """home page for pizzas."""
    return render(request, "pizzas/index.html")


def pizzas(request):
    pizzas = Pizza.objects.order_by("date_added")

    context = {"pizzas": pizzas}

    return render(request, "pizzas/topics.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    entries = pizza.toppings_set.order_by("-date_added")

    context = {"pizza": pizza, "entries": entries}

    return render(request, "pizzas/topic.html", context)


def new_pizza(request):
    if request.method != "POST":
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("pizzas:pizzas")
    context = {"form": form}
    return render(request, "pizzas/new_topic.html", context)
