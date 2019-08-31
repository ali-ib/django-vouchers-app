from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.views.generic import FormView
from .forms import CheckForm
from .models import Voucher

# ---------------------------------------------------------------------------------
# This view built based on FormView and is responsible for rendering the check page
# ---------------------------------------------------------------------------------
class CheckView(FormView):
    template_name = 'vouchers/check_code.html'
    form_class = CheckForm
    success_url = '/result/'

    def form_valid(self, form):
        result = self.check_code(form.cleaned_data['code'])
        self.request.session['result'] = result
        return super(CheckView, self).form_valid(form)

    def check_code(self, code):
        """
        Checks the validity of the entered code and returns the result
        """
        try:
            voucher = Voucher.objects.get(code=code)
            if voucher.remaining_uses > 0:
                msg = "Voucher code is valid, your discount = %s" % voucher.get_discount_value()
                valid = True
                voucher.remaining_uses -= 1
                voucher.save()
            else:
                msg = "Voucher code has been redeemed."
                valid = False

        except Voucher.DoesNotExist as err:
            msg = "Voucher code is invalid"
            valid = False

        return {'valid': valid, 'msg': msg}

# ------------------------------------------------------------------------------------
# This view recieves the check result and is responsible for rendering the result page
# ------------------------------------------------------------------------------------
def result_view(request):
    if 'result' in request.session:
        result = request.session['result']
        del request.session['result']
        return render(request, 'vouchers/result.html', result)

    else:
        return render(request, 'vouchers/result.html', {'valid': False, 'msg': 'Bad request! You reached this page incorrectly.'})
    
