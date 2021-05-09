from django.shortcuts import render, redirect

# Create your views here.
import requests
from datetime import date
from .models import *


def category_view(request):
    categories = Category.objects.all()
    # search = ''

    # if request.method == 'POST':
    #     task = request.POST.get('task')
    #     delete = request.POST.get('delete')
    #
    #     if task != '' and task != None:
    #         # Tasks.objects.create(text=task)
    #         return redirect('/')
    #
    #     if request.POST.get('search') != '':
    #         search = request.POST.get('search')
    #
    #     if delete != '' and delete != None:
    #         # Tasks.objects.get(id=delete).delete()
    #         return redirect('/')

    context = {
        'categories': categories,
        # 'filter': search
    }

    return render(request, 'category.html', context)


def subcategory_view(request, category_name):
    subcategories = Subcategory.objects.all()

    context = {
        'subcategories': subcategories,
    }

    return render(request, 'subcategory.html', context)


def product_view(request, category_name, subcategory_name):
    product = Product.objects.all()

    context = {
        'product': product,
    }

    return render(request, 'product.html', context)
