from ..models import AccountConfirmation


def accept_confirmation(username, token, confirmation_type):
    """
    Подтверждение токена
    """
    __use_confirmation(username, token, confirmation_type)


def __use_confirmation(username, token, confirmation_type):
    account_confirmation = AccountConfirmation.objects.get(
        user__username=username
        , token=token
        , confirmation_type=confirmation_type
    )
    account_confirmation.is_used = True
    account_confirmation.save()
