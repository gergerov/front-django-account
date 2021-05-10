from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from ..forms import base_elements as b


def is_exists_email(email):
    if not User.objects.filter(email=email).exists():
        raise ValidationError(
            _('пользователя с таким email не существует'),
        )


class UserResetPasswordSendForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserResetPasswordSendForm, self).__init__(*args, **kwargs)

        self.fields['email'].validators = [is_exists_email]
        self.fields['email'].help_text = 'We will send you an email with instructions on how to reset your password'

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                '',
                'email',
            ),
            HTML('<div class="container-fluid h-100 w-100 p-0 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1">'),
            b.send_reset_password_link,
            b.home_link,
            b.login_link,
            b.registration_link,
            HTML('</div>'),
        )
