from django.contrib import admin
from .models import Customer, CustomerMessage, CustomerMessageThread

# Register your models here.

class CustomerMessageAdminInline(admin.TabularInline):
    model = CustomerMessage
    fields = (
        'user',
        'date',
        'body',
    )
    
    readonly_fields = (
        'user',
        'date',
        'body',
    )


class CustomerMessageThreadAdmin(admin.ModelAdmin):
    inlines = (CustomerMessageAdminInline,)

    readonly_fields = ('order_number','user_email', 'subject',)
    ordering = ('created',)


admin.site.register(Customer)
admin.site.register(CustomerMessageThread, CustomerMessageThreadAdmin)