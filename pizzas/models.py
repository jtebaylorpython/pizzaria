from django.db import models


class Pizza(models.Model):
    """Type of pizzas."""

    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.name


class Toppings(models.Model):
    """Specific types of pizzas"""

    topic = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Pizza Toppings"

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
