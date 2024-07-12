from django.apps import AppConfig


class OrdersConfig(AppConfig):
    """
    App for creating or updating an Order instance.

    This app is based on the Orders
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
