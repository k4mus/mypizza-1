from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for creating or updating an Order instance.

    This form is based on the Order model and includes fields
    for pizza_type and comments.
    """
    class Meta:
        model = Order
        fields = ['pizza_type', 'comments']
