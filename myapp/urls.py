from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('about', views.about, name='about'),
    path('categories', views.categories, name='categories'),
    path('products', views.products, name='products'),
    
    
]