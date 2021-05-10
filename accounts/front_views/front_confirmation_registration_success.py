from django.shortcuts import render, redirect
from django.views import View


class ConfirmationRegistrationSuccess(View):
    template = 'account/confirmation_registration_success.html'
    title = 'confirmation registration success'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            template_name=self.template,
            context={'title': self.title}
        )
