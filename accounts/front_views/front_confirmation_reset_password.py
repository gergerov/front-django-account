from django.shortcuts import render, redirect
from django.views import View

from ..forms.confirmation_form import ConfirmationResetPasswordForm

from ..validators.base import *
from ..validators.confirmations_validators import *

from ..services.confirmation import accept_confirmation
from ..services.accept_reset_password import accept_reset_password

from ..exceptions import *


class ConfirmationResetPassword(View):
    template = 'account/confirmation_reset_password.html'
    title = 'confirmation reset password'

    def get(self, request, *args, **kwargs):
        form = ConfirmationResetPasswordForm()
        context = {
            'title': self.title
            , 'form': form
        }
        return render(
            request
            , template_name=self.template
            , context=context
        )

    def post(self, request, *args, **kwargs):

        self.request_data = request.POST
        self.username = request.POST["username"]
        self.token = request.POST["token"]
        self.confirmation_type = "RESET"

        try:
            is_exists_token(self.username, self.token, self.confirmation_type)
            is_used_token(self.username, self.token, self.confirmation_type)
            is_not_exists_user(self.username)
            is_active_user(self.username)

        except (IncorrectRequestData, IncorrectConfirmationType,
                DoesNotExistsConfirmation, UsedConfirmation,
                DoesNotExistsUsername, InactiveUser) as e:
            form = ConfirmationResetPasswordForm(request.POST)
            form.add_error(error=e.message, field='token')

            context = {
                'title': self.title
                , 'form': form
            }
            return render(
                request
                , template_name=self.template
                , context=context
            )

        accept_confirmation(self.username, self.token, self.confirmation_type)
        accept_reset_password(self.username, self.request_data["new_password"])


        return redirect('front_reset_password_success')
