from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):

    if Product.objects.count() == 0:

        Product.objects.create(
            name="Nike Air Max",
            description="Premium running shoe",
            price=4999,
            image="https://images.unsplash.com/photo-1542291026-7eec264c27ff"
        )

        Product.objects.create(
            name="Adidas Ultraboost",
            description="Comfortable sports shoe",
            price=6999,
            image="https://images.unsplash.com/photo-1543508282-6319a3e2621f"
        )

        Product.objects.create(
            name="Puma Velocity",
            description="Lightweight performance shoe",
            price=3999,
            image="https://images.unsplash.com/photo-1600185365483-26d7a4cc7519"
        )

    products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {
            'products': products
        }
    )


def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        'products/product_detail.html',
        {
            'product': product
        }
    )