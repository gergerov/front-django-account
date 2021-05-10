from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML

from accounts.forms import base_elements as b


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'only Latin characters, numbers, dots'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'password',
            ),
            HTML('<div class="container-fluid h-100 w-100 p-0 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1">'),
            b.login_submit,
            b.forgot_password_link,
            b.registration_link,
            b.home_link,
            HTML('</div>'),
        )