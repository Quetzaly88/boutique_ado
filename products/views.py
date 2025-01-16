from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# product view
def all_products(request):
    """A view show all products, including sorting and search queries
    """

    products = Product.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

# product detail view
def product_detail(request, product_id):
    """A view show aindividual product details
    """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products.html', context)