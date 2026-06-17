from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.models import CartItem


def checkout(request):

    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = CartItem.objects.filter(
        user=request.user
    )

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

    return redirect('order_success')


def order_history(request):

    if not request.user.is_authenticated:
        return redirect('login')

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'orders/order_history.html',
        {
            'orders': orders
        }
    )


def order_success(request):

    return render(
        request,
        'orders/order_success.html'
    )