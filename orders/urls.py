from django.urls import path
from .views import checkout, order_history, order_success

urlpatterns = [

    path(
        'checkout/',
        checkout,
        name='checkout'
    ),

    path(
        'history/',
        order_history,
        name='order_history'
    ),

    path(
    'success/',
    order_success,
    name='order_success'
),
]