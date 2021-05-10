from django.contrib.auth.models import User


def activate_user(username):
    """
    Активирует пользователя
    """

    user = User.objects.get(username=username)
    user.is_active=True
    user.save()