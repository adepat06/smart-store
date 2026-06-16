from django.shortcuts import redirect
from .models import Order, OrderItem
from cart.models import CartItem


def checkout(request):

    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = CartItem.objects.all()

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    order = Order.objects.create(
        user=request.user,
        total_price=total
    )

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    cart_items.delete()

    return redirect('/')