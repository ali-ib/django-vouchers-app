from django.db import models
from django.utils.crypto import get_random_string
from string import ascii_uppercase, digits

def generate_code():
    """
    A helper function for generating new, random, unique voucher codes
    """
    codes = Voucher.objects.values_list('code', flat=True)
    code = get_random_string(length = 12, allowed_chars = ascii_uppercase + digits)
    while code in codes:
        code = get_random_string(length = 12, allowed_chars = ascii_uppercase + digits)
    
    return code

# Create your models here.
class Voucher(models.Model):
    DISCOUNT_CHOICES = (
        (1, 'RM 10'),
        (2, '10% off'),
    )

    code = models.CharField(max_length=12, editable=False, default=generate_code)
    discount = models.IntegerField(default=1, choices=DISCOUNT_CHOICES)
    remaining_uses = models.IntegerField(default=3, editable=False)

    def get_discount_value(self):
        return dict(self.DISCOUNT_CHOICES).get(self.discount)

    def __str__(self):
       return self.code