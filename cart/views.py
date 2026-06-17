from django.shortcuts import render, redirect
from .models import CartItem
from products.models import Product


def add_to_cart(request, product_id):

    if not request.user.is_authenticated:
        return redirect('login')

    product = Product.objects.get(
        id=product_id
    )

    quantity = int(
        request.POST.get('quantity', 1)
    )

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if created:
        cart_item.quantity = quantity
    else:
        cart_item.quantity += quantity

    cart_item.save()

    return redirect(f'/product/{product.id}/')

def cart_view(request):

    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = CartItem.objects.filter(
        user=request.user
    )

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