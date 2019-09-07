from django import forms
from django.core.validators import RegexValidator


class CheckForm(forms.Form):
    """This custom form defines the code-check form.

    Attributes:
        code (CharField): A char field to enter the code.
    """

    code = forms.CharField(label='', max_length=12, validators=[RegexValidator(
        '^[A-Z0-9]{12}$', message="Invalid voucher code format.")])

    def __init__(self, *args, **kwargs):
        """Inits the generated form."""
        super(CheckForm, self).__init__(*args, **kwargs)

        # Set the placeholder of the code field.
        self.fields['code'].widget.attrs['placeholder'] \
            = 'Enter your Voucher Code here'

        # Add 'text-center' class to the code field.
        self.fields['code'].widget.attrs['class'] = 'text-center'
