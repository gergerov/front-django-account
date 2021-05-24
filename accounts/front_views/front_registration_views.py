from django.shortcuts import render, redirect
from django.views import View

from accounts.forms.user_registration_form import UserRegistrationForm
from accounts.services.registration import registration_user


class RegistrationView(View):
    template = 'account/registration.html'
    title = 'Register'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            registration_form = UserRegistrationForm()
            return render(
                request, 'account/registration.html',
                {'form': registration_form, 'title': self.title}
            )

    def post(self, request, *args, **kwargs):
        try:
            # отправим домой, если авторизован
            if request.user.is_authenticated:
                return redirect('home')

            registration_user(
                username=request.POST['username']
                , email=request.POST['email']
                , password=request.POST['password']
            )
            return redirect('front_registration_success')

        except Exception as e:
            form = UserRegistrationForm(request.POST)
            form.add_error(field='username', error=str(e))

        return render(request, self.template, {'form': form, 'title': self.title})
