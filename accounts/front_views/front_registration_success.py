from django.shortcuts import render, redirect
from django.views import View


class RegistrationSuccess(View):
    template = 'account/registration_success.html'
    title = 'Success registration'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            template_name=self.template,
            context={'title': self.title}
        )
