from django.shortcuts import render


def base(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/aboutUs.html')

def categories(request):
    return render(request, 'pages/product_categories.html')

def products(request):
    return render(request, 'pages/products.html')