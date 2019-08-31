from django.contrib import admin
from .models import Voucher

class VoucherAdmin(admin.ModelAdmin):
    readonly_fields=('code', 'remaining_uses')
    list_display = ('code', 'discount', 'remaining_uses')

# Register your models here.
admin.site.register(Voucher, VoucherAdmin)