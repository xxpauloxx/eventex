from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        form = SubscriptionForm()
        """Form must have four fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits."""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def test_name_must_be_captalized(self):
        """Name must be captalized."""
        form = self.make_validated_form(name='PAULO Roberto')
        self.assertEqual('Paulo Roberto', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email must be optional."""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone must be optional."""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_phone_none_email_invalid(self):
        form = self.make_validated_form(phone='', email='pauloroberto.info')
        self.assertIn('email', form.errors)

    def test_inform_email_or_phone(self):
        """Email and form are optional, but one must be informed."""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Paulo Roberto', cpf='12345678901',
                    email='paulo.pinda@gmail.com', phone='12-99221-8616')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form