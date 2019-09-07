from string import ascii_uppercase, digits
from decimal import Decimal
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def generate_code():
    """A helper function for generating new voucher codes.

    Returns:
        new_code (str): The new, unique, generated code.
    """
    old_codes = Voucher.objects.values_list('code', flat=True)
    new_code = get_random_string(
        length=12, allowed_chars=ascii_uppercase + digits)
    while new_code in old_codes:
        new_code = get_random_string(
            length=12, allowed_chars=ascii_uppercase + digits)

    return new_code


class Voucher(models.Model):
    """A Model class defines the Voucher model.

    Attributes:
        DISCOUNT_FORMATS (constant): The available formats for the discount.
        code (CharField): A char field displays the generated code value.
        discount_format (IntegerField): The format of the discount.
        discount_value (DecimalField): The value of the discount.
        remaining_uses (IntegerField): The total remaining uses for
            this voucher code.
    """

    DISCOUNT_FORMATS = (
        (1, 'RM '),
        (2, '% off'),
    )

    code = models.CharField(
        max_length=12, editable=False, default=generate_code)
    discount_value = models.DecimalField(
        default=10, max_digits=5, decimal_places=1,
        validators=[
            MinValueValidator(Decimal('0'))
        ]
    )
    discount_format = models.IntegerField(default=1, choices=DISCOUNT_FORMATS)
    remaining_uses = models.IntegerField(default=3, editable=False)

    def clean(self):
        """Validates the dicount value in case of percent format.

        This method overrides the Model.clean() method to ensure
        that the discount value is between 0 and 100 if the selected
        format is the precent format.
        """
        if self.discount_format == 2:
            if self.discount_value > 100:
                raise ValidationError()

    def get_discount_value(self):
        """This method maps discount format id to its value"""
        format = dict(self.DISCOUNT_FORMATS).get(self.discount_format)
        value = self.discount_value
        if self.discount_format == 1:
            return f"{format}{value}"
        else:
            return f"{value}{format}"

    def still_valid(self):
        """Checks if the voucher code has any remaining uses."""
        return self.remaining_uses > 0

    def redeem_code(self):
        """Redeems the voucher code."""
        if self.remaining_uses > 0:
            self.remaining_uses -= 1

    def __str__(self):
        return self.code
