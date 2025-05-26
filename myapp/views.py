from django.shortcuts import render
from .models import Category, Product 
from django.shortcuts import get_object_or_404

def base(request):
    categories = Category.objects.all()
    bestselling = Product.objects.filter(is_bestsell=True, is_active=True)

    row1 = [prod for i, prod in enumerate(bestselling) if i % 2 == 0]
    row2 = [prod for i, prod in enumerate(bestselling) if i % 2 == 1]

    return render(request, 'pages/home.html', {'categories': categories, 'row1': row1,
        'row2': row2,})

def about(request):
    return render(request, 'pages/aboutUs.html')

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def categories(request):
    categories = Category.objects.all()
    return render(request, 'pages/product_categories.html', {'categories': categories})

def products(request, name):
    category = get_object_or_404(Category, name=name)
    products = Product.objects.filter(category=category)
    
    return render(request, 'pages/products.html', {
        'products': products,
        'selected_category': category,
        'category_name': category.name,
    })

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_details(request, id):
    product = get_object_or_404(Product, id=id)

    # Ensure product has a valid category and category name
    if not product.category or not product.category.name:
        product.category = None

    return render(request, 'section/product_details.html', {'product': product})


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



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, MyCart

# ✅ ADD TO CART
@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if cart item exists for this user and product
    cart_item, created = MyCart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, "Product quantity updated in your cart.")
    else:
        messages.success(request, "Product added to your cart.")

    return redirect('cart')  # name of the view for the cart page


# ✅ VIEW CART
@login_required(login_url='login')
def view_cart(request):
    cart_items = MyCart.objects.filter(user=request.user)  # Only current user's items
    total = sum(item.subtotal() for item in cart_items)  # Total for current user
    return render(request, 'pages/mycart.html', {
        'cart_items': cart_items,
        'total': total
    })


# ✅ REMOVE FROM CART
@login_required
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    MyCart.objects.filter(user=request.user, product=product).delete()
    return redirect('cart')

from django.http import JsonResponse
from .models import MyCart
from django.http import JsonResponse
from .models import MyCart

@login_required
def update_cart_quantity(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        action = request.POST.get('action')

        try:
            cart_item = MyCart.objects.get(id=cart_id, user=request.user)
            if action == 'increase':
                cart_item.quantity += 1
            elif action == 'decrease':
                cart_item.quantity -= 1
                if cart_item.quantity <= 0:
                    cart_item.delete()
                    total = sum(item.product.price * item.quantity for item in MyCart.objects.filter(user=request.user))
                    return JsonResponse({'success': True, 'quantity': 0, 'total': total})

            cart_item.save()
            subtotal = cart_item.product.price * cart_item.quantity
            total = sum(item.product.price * item.quantity for item in MyCart.objects.filter(user=request.user))

            return JsonResponse({
                'success': True,
                'quantity': cart_item.quantity,
                'subtotal': subtotal,
                'total': total
            })
        except MyCart.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Cart item not found.'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import MyCart
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import MyCart, Order, OrderItem, Product

from django.shortcuts import render, redirect
from .models import Order, OrderItem
from myapp.models import MyCart  # Assuming your cart model is in myapp
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyCart, Order, OrderItem

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlencode
from .models import MyCart, Order, OrderItem
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from urllib.parse import urlencode
from .models import MyCart, Order, OrderItem

from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyCart, Order, OrderItem

@login_required
def checkout(request):
    user = request.user
    cart_items = MyCart.objects.filter(user=user)

    if not cart_items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect('cart')

    if request.method == "POST":
        # Get user data from form
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        pincode = request.POST.get("pincode")
        city = request.POST.get("city")
        district = request.POST.get("district")
        state = request.POST.get("state")
        payment_method = request.POST.get("payment_method")

        # Calculate total
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        # Create Order
        order = Order.objects.create(
            user=user,
            full_name=full_name,
            email=email,
            mobile=mobile,
            pincode=pincode,
            city=city,
            district=district,
            state=state,
            payment_method=payment_method,
            total_price=total_price,
            payment_status='Unpaid'
        )

        # Create OrderItems
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Clear cart
        cart_items.delete()

        # Generate UPI link
        upi_id = 'boopesh.3083@oksbi'
        payee_name = 'Boopesh Prasanth'
        transaction_note = f'Order #{order.id} payment'

        upi_url = (
            "upi://pay?" + urlencode({
                'pa': upi_id,
                'pn': payee_name,
                'tn': transaction_note,
                'am': str(total_price),
                'cu': 'INR'
            })
        )

        # For GPay, PhonePe, or Paytm, show same UPI link (they handle it via app)
        if payment_method in ['GPay', 'PhonePe', 'Paytm']:
            return render(request, 'pages/payment.html', {
                'upi_url': upi_url,
                'order': order,
                'payment_method': payment_method
            })

        # For other payment methods
        messages.success(request, "Your order has been placed successfully!")
        return redirect('home')

    return render(request, 'pages/checkout.html')




from django.shortcuts import render, get_object_or_404
from .models import Order
from urllib.parse import quote

@login_required
def pay_with_gpay(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    upi_id = "yourupi@okaxis"  # ✅ Your UPI ID here
    name = "Your Business Name"
    txn_note = f"Order#{order.id}"
    amount = str(order.total_price)
    transaction_ref = f"TID{order.id}XYZ"

    gpay_url = (
        f"https://pay.google.com/gp/p/ui/pay?"
        f"pa={upi_id}&pn={quote(name)}&mc=0000"
        f"&tid={transaction_ref}&tr={transaction_ref}"
        f"&tn={quote(txn_note)}&am={amount}&cu=INR"
    )

    return render(request, "payment_gpay.html", {"gpay_url": gpay_url, "order": order})

