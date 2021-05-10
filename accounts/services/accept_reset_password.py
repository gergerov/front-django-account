from django.contrib.auth.models import User


def accept_reset_password(username, password):
    """
    Меняет пароль пользователя
    """

    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()