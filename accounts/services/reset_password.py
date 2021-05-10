from ..models import AccountConfirmation
from django.contrib.auth.models import User


def reset_password(username):
    user = User.objects.get(
        username=username,
    )
    confirmation = __create_reset_password_confirmation(user)
    confirmation.send()


def __create_reset_password_confirmation(user) -> AccountConfirmation:
    """
        Создаёт токен подтверждения
        сброса пароля пользователя
        """
    account_confirmation = AccountConfirmation.objects.create(
        user=user
        , confirmation_type='RESET'
        , object_id=user.pk
        , is_used=False
    )

    return account_confirmation
