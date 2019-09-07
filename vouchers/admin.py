from django.contrib import admin
from .models import Voucher


class VoucherAdmin(admin.ModelAdmin):
    """A custom ModelAdmin to define fields properties.

    Attributes:
        readonly_fields (tuple): A tuple of disabled fields.
        list_display (tuple): A tuple indicates the order in which
            the form fields will be displayed.
    """

    readonly_fields = ('code', 'remaining_uses')
    list_display = ('code', 'discount_value',
                    'discount_format', 'remaining_uses')


# Register your models here.
admin.site.register(Voucher, VoucherAdmin)
