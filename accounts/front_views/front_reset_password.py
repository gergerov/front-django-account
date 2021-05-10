from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User


from accounts.forms.reset_password_form import UserResetPasswordSendForm
from accounts.services.reset_password import reset_password


class ResetPasswordView(View):
    template = 'account/reset_password.html'
    title = 'Reset password'

    def get(self, request, *args, **kwargs):
        form = UserResetPasswordSendForm()
        context = {'form': form, 'title': self.title}
        return render(request, self.template, context=context)

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.POST['email'])
        form = UserResetPasswordSendForm(request.POST)

        if not user:
            form.add_error('There is no user with this email address', 'email')
            context = {'form': form, 'title': self.title}
            return render(request, self.template, context=context)
        else:
            username = User.objects.get(email=request.POST['email'])
            reset_password(username)
            return redirect('front_reset_password_sended')

