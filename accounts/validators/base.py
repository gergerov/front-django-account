from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from ..exceptions import *

import re

lat_chars_and_nums = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.'


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
            raise IncorrectUsername


def is_exists_username(username):
    if User.objects.filter(username=username).exists():
        raise ExistsUsername


def is_not_exists_user(username):
    is_exists_user = User.objects.filter(username=username).exists()
    if not is_exists_user:
        raise DoesNotExistsUsername


def is_correct_email(email):
    """
    Слизанная с просторов регулярочка.
    Говорит, является ли тект email-адресом (формат, не более).
    Так же проверяем, есть ли такое мыло в БД уже.
    """
    pattern = re.compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    is_valid = pattern.match(email)

    if not is_valid:
        raise IncorrectEmail


def is_exists_email(email):
    if User.objects.filter(email=email).exists():
        raise ExistsEmail


def is_correct_account_profile_type(account_profile_type):
    # проверка на корректность типа профиля
    account_profile_types = ['AIRCOMPANY', 'GENERAL_AGENT', 'AGENT', 'AIRPORT', 'CARGO_PLAYER']
    if account_profile_type not in account_profile_types:
        raise IncorrectAccountProfileType


def auth_user(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        raise IncorrectUsernameOrPassword


def is_active_user(username):
    user = User.objects.get(username=username)
    if not user.is_active:
        raise InactiveUser