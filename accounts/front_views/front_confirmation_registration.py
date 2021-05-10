from django.shortcuts import render, redirect
from django.views import View

from ..forms.confirmation_form import ConfirmationRegistrationForm

from ..validators.base import *
from ..validators.confirmations_validators import *

from ..services.confirmation import accept_confirmation
from ..services.activate_user import activate_user

from ..exceptions import *


class ConfirmationRegistration(View):
    template = 'account/confirmation_registration.html'
    title = 'confirmation registration'

    def get(self, request, *args, **kwargs):
        form = ConfirmationRegistrationForm()
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
        self.confirmation_type = "REG"

        try:
            is_exists_token(self.username, self.token, self.confirmation_type)
            is_used_token(self.username, self.token, self.confirmation_type)
            is_not_exists_user(self.username)

        except (IncorrectRequestData, IncorrectConfirmationType,
                DoesNotExistsConfirmation, UsedConfirmation,
                DoesNotExistsUsername, InactiveUser) as e:
            form = ConfirmationRegistrationForm(request.POST)
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

        activate_user(self.username)
        accept_confirmation(self.username, self.token, self.confirmation_type)

        return redirect('front_confirmation_registration_success')


