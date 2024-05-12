from django.contrib import admin
from .models import CustomerOrder, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('video_sub_total',)


class CustomerOrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'order_date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_basket',
                       'stripe_pid')

    fields = ('order_number', 'order_date', 'name',
              'email', 'phone', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_basket',
              'stripe_pid')

    list_display = ('order_number', 'order_date', 'name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-order_date',)

admin.site.register(CustomerOrder, CustomerOrderAdmin)