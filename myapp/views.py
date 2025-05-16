from django.shortcuts import render


def base(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/aboutUs.html')

def categories(request):
    return render(request, 'pages/product_categories.html')

def products(request):
    return render(request, 'pages/products.html')

def signin(request):
    return render(request, 'pages/signin.html')

def product_details(request):
    return render(request, 'pages/product_details.html')

def mycart(request):
    return render(request, 'pages/mycart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def myorder(request):
    return render(request, 'pages/myorder.html')

def watchlist(request):     
    return render(request, 'pages/watchlist.html')

