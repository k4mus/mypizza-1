from django.test import TestCase
from django.urls import reverse
from .models import Order
from .forms import OrderForm

class OrderModelTest(TestCase):
    def test_order_creation(self):
        order = Order.objects.create(pizza_type='Margherita', comments='Extra cheese')
        self.assertEqual(order.pizza_type, 'Margherita')
        self.assertEqual(order.comments, 'Extra cheese')

class OrderViewTest(TestCase):
    def test_place_order_view(self):
        response = self.client.get(reverse('place_order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/place_order.html')

    def test_order_list_view(self):
        Order.objects.create(pizza_type='Pepperoni', comments='No onions')
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_list.html')
        self.assertContains(response, 'Pepperoni')
        self.assertContains(response, 'No onions')

    def test_order_submission(self):
        data = {
            'pizza_type': 'Vegetarian',
            'comments': 'Gluten-free base'
        }
        response = self.client.post(reverse('place_order'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful submission
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.first().pizza_type, 'Vegetarian')
        self.assertEqual(Order.objects.first().comments, 'Gluten-free base')

class OrderFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'pizza_type': 'Vegetarian',
            'comments': 'Gluten-free base'
        }
        form = OrderForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'pizza_type': '',
            'comments': 'Gluten-free base'
        }
        form = OrderForm(data=data)
        self.assertFalse(form.is_valid())
