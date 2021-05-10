from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML
from ..forms import base_elements as b


class ConfirmationResetPasswordForm(forms.Form):
    username = forms.CharField()
    token = forms.UUIDField()
    new_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(ConfirmationResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'token',
                'new_password',
            ),
            HTML('<div class="container-fluid h-100 w-100 p-0 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1">'),
            b.accept_new_password,
            HTML('</div>'),
        )


class ConfirmationRegistrationForm(forms.Form):
    username = forms.CharField()
    token = forms.UUIDField()

    def __init__(self, *args, **kwargs):
        super(ConfirmationRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'token',
                'new_password',
            ),
            HTML('<div class="container-fluid h-100 w-100 p-0 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1">'),
            b.accept_registration,
            HTML('</div>'),
        )