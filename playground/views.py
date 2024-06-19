from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem, Order


def say_hello(request):
    # queryset = Product.objects.values('id', 'title').filter(id=F('orderitem__product_id')).distinct().order_by('title')
    # queryset = Product.objects.values('id', 'title').filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # queryset = OrderItem.objects.filter(order_id__in=queryset)

    # return render(request, 'hello.html', {'name': 'Fardin', 'products': [1, 2]})
    # return render(request, 'hello.html', {'name': 'Fardin', 'products': list(queryset)})
    return render(request, 'hello.html', {'name': 'Fardin', 'orderitems': list(queryset)})
