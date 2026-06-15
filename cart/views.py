from django.shortcuts import render, redirect
from .models import CartItem
from products.models import Product


def add_to_cart(request, product_id):

    product = Product.objects.get(
        id=product_id
    )

    cart_item, created = CartItem.objects.get_or_create(
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def cart_view(request):

    cart_items = CartItem.objects.all()

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return render(
        request,
        'cart/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )