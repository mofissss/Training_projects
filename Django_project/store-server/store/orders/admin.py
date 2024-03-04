from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = (
        'id', 'created',
        ('first_name', 'last_name'),
        ('email', 'delivery_address'),
        'basket_history', 'status', 'user_created_order'
    )
    readonly_fields = ('id', 'created')
