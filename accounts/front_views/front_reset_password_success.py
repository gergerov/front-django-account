from django.shortcuts import render, redirect
from django.views import View


class ResetPasswordSuccess(View):
    template = 'account/reset_password_success.html'
    title = 'Success reset password'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            template_name=self.template,
            context={'title': self.title}
        )
