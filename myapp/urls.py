from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('about/', views.about, name='about'),
    
    path('categories/', views.categories, name='categories'),
    path('products/<str:name>/', views.products, name='products'),
    path('product/<int:id>/', views.product_details, name='product_details'),  # Product Details


    path('signin/', views.signin, name='signin'),
    path('product_details/', views.product_details, name='product_details'),
    path('mycart/', views.mycart, name='mycart'),
    path('checkout/', views.checkout, name='checkout'),
    path('myorder/', views.myorder, name='myorder'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('cart/', views.view_cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/', views.update_cart_quantity, name='update_cart_quantity'),
    # URL for the order success confirmation page

    

]
    
