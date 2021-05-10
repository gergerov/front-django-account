from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import AccountConfirmation


@register(AccountConfirmation)
class AccountProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'confirmation_type', 'is_used', 'date_create', 'object_id' )

