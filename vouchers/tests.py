from django.test import TestCase
from django.urls import reverse
from .models import Voucher


class VoucherModelTests(TestCase):
    """A test case for the Voucher model"""

    def test_voucher_code_with_no_remaining_uses(self):
        """A voucher code with no remaining uses should return
            False when checked for validity.
        """
        voucher_code = Voucher(remaining_uses=0)
        self.assertIs(voucher_code.still_valid(), False)


class CheckCodeViewTests(TestCase):
    """A test case to test the view that renders the check form."""

    def test_view_returns_correct_status_code(self):
        """Tests if the code check page is accessible and returns
            the 200 (success) status code and contains the code field
            placeholder message.
        """
        response = self.client.get(reverse('check'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter your Voucher Code here")


class ResultViewTests(TestCase):
    """A test case to test the view that renders the result page."""

    def test_view_response_to_incorrect_access(self):
        """Tests if the result page responds correctly to illegal access
            that is, trying to access the page without using the check
            form. The page should display a message indicating that.
        """
        response = self.client.get(reverse('result'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Bad request! You reached this page incorrectly."
        )
