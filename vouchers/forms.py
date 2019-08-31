from django import forms
import re

class CheckForm(forms.Form):
    code = forms.CharField(label='', max_length=12)

    def __init__(self, *args, **kwargs):
        super(CheckForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['placeholder'] = 'Enter your Voucher Code here'
        self.fields['code'].widget.attrs['class'] = 'text-center'

    def clean_code(self):
        """
        Custom validator for the code field that makes sure its format is valid
        """
        code = self.cleaned_data['code']
        if not re.match("^[A-Z0-9]{12}$", code):
            raise forms.ValidationError("Invalid voucher code format.")
        return code
