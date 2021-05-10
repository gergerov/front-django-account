from ..exceptions import *
from ..models import AccountConfirmation


def is_exists_token(username, token, confirmation_type):
    """
    Проверяет, существует ли токен подтверждения
    """
    is_exists_confirmation = AccountConfirmation.objects.filter(
        user__username=username
        , token=token
        , confirmation_type=confirmation_type
    ).exists()

    if not is_exists_confirmation:
        raise DoesNotExistsConfirmation


def is_used_token(username, token, confirmation_type):
    """
    Проверяет использвался ли токен
    """
    is_used_token = AccountConfirmation.objects.filter(
        user__username=username
        , token=token
        , confirmation_type=confirmation_type
        , is_used=False
    ).exists()

    if not is_used_token:
        raise UsedConfirmation


def is_correct_confirmation_type(confirmation_type):
    if confirmation_type not in ["REG", "RESET"]:
        raise IncorrectConfirmationType


def is_correct_request_data(request_data):
    if "username" not in request_data:
        raise IncorrectRequestData

    if "token" not in request_data:
        raise IncorrectRequestData

    if "confirmation_type" not in request_data:
        raise IncorrectRequestData

    if request_data["confirmation_type"] == "RESET":
        if "new_password" not in request_data:
            raise IncorrectRequestData






