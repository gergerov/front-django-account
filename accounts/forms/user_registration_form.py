import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from ..forms import base_elements as b

lat_chars_and_nums = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.'


def is_correct_email(email):
    """
    Слизанная с просторов регулярочка.
    Говорит, является ли тект email-адресом (формат, не более).
    Так же проверяем, есть ли такое мыло в БД уже.
    """

    pattern = re.compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    is_valid = pattern.match(email)

    if not is_valid:
        raise ValidationError(
            _('неправильный email адрес'),
        )
    if User.objects.filter(email=email).exists():
        raise ValidationError(
            _('пользователь с таким email уже существует'),
        )


def is_correct_username(username):
    """
    Считаю такой набор символов достаточным
    для требований к имени пользователя.
    Так же проверят существование пользователя
    С аналогичным именем в БД.
    """
    # допускаем только латинские символы, цифры и точку
    for char in username:
        if char not in lat_chars_and_nums:
            raise ValidationError(
                _('поле может содержать только латинские символы, цифры, точки'),
            )

    if User.objects.filter(username=username).exists():
        raise ValidationError(
            _('пользователь с таким именем уже существует'),
        )


class UserRegistrationForm(forms.ModelForm):
    """Форма регистрации пользователя"""
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # делаем мыло обязательным, т.к. в джанговом юзере это не обязательно
        self.fields['email'].required = True
        self.fields['email'].help_text = 'A confirmation email will be sent to this address'
        self.fields['email'].label = 'Email address'
        self.fields['email'].validators = [is_correct_email]

        self.fields['username'].help_text = 'Will be used for input (only Latin characters, numbers, dots)'
        self.fields['username'].label = 'Login'
        self.fields['username'].validators = [is_correct_username]

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'email',
                'password',
                'password2'
            ),
            HTML('<div class="container-fluid h-100 w-100 p-0 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1">'),
            b.registration_submit,
            b.forgot_password_link,
            b.login_link,
            b.home_link,
            HTML('</div>'),
            )

    # пока что так, не в валидаторе, т.к. не знаю как
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')

        return cd['password2']