from django.contrib import admin
from .models import Customer, CustomerMessage, CustomerMessageThread

# Register your models here.

class CustomerMessageAdminInline(admin.TabularInline):
    model = CustomerMessage
    fields = (
        'user',
        'date',
        'user_email',
        'subject',
        'body',
    )
    
    readonly_fields = (
        'user',
        'date',
        'user_email',
        'subject',
        'body',
    )


class CustomerMessageThreadAdmin(admin.ModelAdmin):
    inlines = (CustomerMessageAdminInline,)

    readonly_fields = ('order_number',)
    ordering = ('created',)


admin.site.register(Customer)
admin.site.register(CustomerMessageThread, CustomerMessageThreadAdmin)