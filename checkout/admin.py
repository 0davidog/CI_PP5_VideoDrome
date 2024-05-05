from django.contrib import admin
from .models import Order, OrderBasket


class OrderBasketAdminInline(admin.TabularInline):
    model = OrderBasket
    readonly_fields = ('basket_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderBasketAdminInline,)

    readonly_fields = ('order_number', 'order_date',
                       'delivery_cost', 'order_total',
                       'order_total',)

    fields = ('order_number', 'order_date', 'first_name', 'last_name',
              'email', 'phone', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'basket_total', 'order_total',)

    list_display = ('order_number', 'order_date', 'first_name', 'last_name',
                    'basket_total', 'delivery_cost',
                    'order_total',)

    ordering = ('-order_date',)

admin.site.register(Order, OrderAdmin)