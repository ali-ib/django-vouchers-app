from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.views.generic import FormView
from .forms import CheckForm
from .models import Voucher


class CheckView(FormView):
    """A FormView-type view to render the check form page.

    Attributes:
        template_name (str): The path of the view template.
        form_class (Form): The custom form class used to define the check form.
        success_url (str): The url to be redirected to if the form is valid.
    """

    template_name = 'vouchers/check_code.html'
    form_class = CheckForm
    success_url = '/result/'

    def form_valid(self, form):
        """Handles the submitted form data.

        Attributes:
            form (form): An instance of the submitted form.
        """

        # Call check_code function on code value
        result = self.check_code(form.cleaned_data['code'])

        # Stote the check result in the session
        self.request.session['result'] = result
        return super(CheckView, self).form_valid(form)

    def check_code(self, code):
        """Checks the validity of the entered code.

        Args:
            code (str): The value of the code to be checked.

        Returns:
            result (dict): A dicionary contains the result of the check.
        """

        try:
            # Check if the code is valid
            voucher = Voucher.objects.get(code=code)

            # Check if the valid code in not completely redeemed
            if voucher.still_valid():
                message = "Voucher code is valid, your discount = %s" \
                    % voucher.get_discount_value()
                valid = True
                voucher.redeem_code()
                voucher.save()
            else:
                message = "Voucher code has been redeemed."
                valid = False

        except Voucher.DoesNotExist as err:
            message = "Voucher code is invalid"
            valid = False

        return {'valid': valid, 'message': message}


def result_view(request):
    """This view renders the result page.

    Args:
        request (HttpRequest object): The request object passed to the view.

    Returns:
        A HttpResponse rendered using the 'render' function.
    """

    if 'result' in request.session:
        result = request.session['result']
        del request.session['result']
        return render(request, 'vouchers/result.html', result)

    else:
        return render(
            request,
            'vouchers/result.html',
            {
                'valid': False,
                'message': 'Bad request! You reached this page incorrectly.'
            }
        )
