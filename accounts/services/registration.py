from django.contrib.auth.models import User
from ..models import AccountConfirmation


def registration_user(username, password, email):
    user = __create_user(username, password, email)['user']
    confirmation = __create_registration_confirmation(user)
    confirmation.send()


def __create_user(username, password, email):
    """
    Создаёт базового пользователя
    а также его профиль
    """

    user = User.objects.create(
        username=username,
        email=email,
        is_active=False
    )

    user.set_password(password)
    user.save()
    return {'user': user}


def __create_registration_confirmation(user: User):
    """
    Создаёт токен подтверждения
    электронной почты пользователя
    """
    account_confirmation = AccountConfirmation.objects.create(
        user=user
        , confirmation_type='REG'
        , object_id=user.pk,
        is_used=False)

    return account_confirmation
