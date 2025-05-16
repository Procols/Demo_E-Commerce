from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    path('signin', views.signin, name='signin'),
    path('product_details/', views.product_details, name='product_details'),
    path('mycart/', views.mycart, name='mycart'),
    path('checkout/', views.checkout, name='checkout'),
    path('myorder/', views.myorder, name='myorder'),
    path('watchlist/', views.watchlist, name='watchlist'),
    
    
]