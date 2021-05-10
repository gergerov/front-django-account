from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

import uuid

CONFIRMATION_TYPES = [
    ('REG', 'Регистрация'),  # Используется для подтверждения регистрации
    ('RESET', 'Сброс пароля')  # Используется для сброса пароля
]


class AccountConfirmation(models.Model):

    """
    Класс для хранения uuid подтверждений.
    Для других операций с электронной почтой
    На один мэил подтверждение
    регистрации отправляется единожды.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    token = models.UUIDField(unique=False, default=uuid.uuid4, verbose_name="токен")
    confirmation_type = models.CharField(max_length=10, null=False, choices=CONFIRMATION_TYPES)
    is_used = models.BooleanField(null=False, default=False)
    date_create = models.DateTimeField(default=timezone.now)
    object_id = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return f'Токен подтверждения пользователя {self.user} вида {self.confirmation_type}'

    def send(self):
        try:
            EMAIL_CONFIRMATIONS_URL_RESET_PASSWORD = settings.EMAIL_CONFIRMATIONS_URL_RESET_PASSWORD
            EMAIL_CONFIRMATIONS_URL_REGISTRATION = settings.EMAIL_CONFIRMATIONS_URL_REGISTRATION
        except:
            EMAIL_CONFIRMATIONS_URL_RESET_PASSWORD = 'http://127.0.0.1:8000/accounts/front/confirmation_reset_password'
            EMAIL_CONFIRMATIONS_URL_REGISTRATION = 'http://127.0.0.1:8000/accounts/front/confirmation_registration'

        email = [self.user.email]
        send_from = 'accounts'
        if self.confirmation_type == "REG":
            url = EMAIL_CONFIRMATIONS_URL_REGISTRATION
        if self.confirmation_type == "RESET":
            url = EMAIL_CONFIRMATIONS_URL_RESET_PASSWORD

        link = url + '/'

        text = f'' \
               f'URL for confirming the action : {link} . ' \
               f'Data for confirmation: ' \
               f'"username" {self.user.username} , ' \
               f'"token" {self.token} , ' \
               f'"confirmation_type" {self.confirmation_type} , ' \
               f'"object_id" {self.object_id} . '
        topic = f'User Action Confirmation ({self.confirmation_type}).'
        send_mail(topic, text, send_from, email)

