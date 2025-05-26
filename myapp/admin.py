from django.contrib import admin
from .models import Category, Product, MyCart, Order, OrderItem


# Inline display of OrderItems inside Order admin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price', 'subtotal']

    def subtotal(self, obj):
        return obj.price * obj.quantity
    subtotal.short_description = 'Subtotal'


# Admin for Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'full_name', 'mobile', 'email', 'full_address',
        'total_price', 'payment_method', 'payment_status', 'created_at'
    ]
    search_fields = ['user__username', 'full_name', 'mobile', 'email']
    list_filter = ['payment_method', 'payment_status', 'created_at']
    inlines = [OrderItemInline]
    readonly_fields = ['full_address', 'total_price']

    def full_address(self, obj):
        return f"{obj.city}, {obj.district}, {obj.state} - {obj.pincode}"
    full_address.short_description = "Address"


# Admin for OrderItem model
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity', 'price', 'subtotal', 'created_at']
    search_fields = ['order__id', 'product__name']
    list_filter = ['created_at']

    def subtotal(self, obj):
        return obj.price * obj.quantity
    subtotal.short_description = "Subtotal"


# Register your models
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(MyCart)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
