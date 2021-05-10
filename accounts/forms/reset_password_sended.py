from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from ..forms import base_elements as b


class UserResetPasswordSendedForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserResetPasswordSendedForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<div class="container-fluid h-100 w-100 p-0 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1">'),
            HTML(
                '<div class="jumbotron">'
                    '<h4 class="display-4">'
                    'Reset password instruction sended!'
                    '</h4>'
                '</div>'
            ),
            HTML('</div>'),
        )