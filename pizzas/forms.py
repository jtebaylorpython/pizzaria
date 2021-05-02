from django import forms

from .models import Pizza, Comment


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["name"]
        labels = {"name": ""}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        labels = {"text": ""}
