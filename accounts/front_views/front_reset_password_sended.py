from django.shortcuts import render, redirect
from django.views import View
from accounts.forms.reset_password_sended import UserResetPasswordSendedForm


class ResetPasswordSendedView(View):
    template = 'account/reset_password_sended.html'
    title = 'Reset password sended'

    def get(self, request, *args, **kwargs):
        form = UserResetPasswordSendedForm()
        context = {'title': self.title, 'form': form}
        return render(request, self.template, context=context)