from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

from ..forms.login_form import LoginForm


class LoginView(View):
    template = 'account/login.html'
    title = 'Authorization'

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('/')
        else:
            form = LoginForm()
            return render(
                request
                , template_name=self.template
                , context={'form': form, 'title': self.title}
            )

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form.add_error(error='Invalid username or password', field='password')
            return render(
                request
                , template_name=self.template
                , context={'form': form, 'title': self.title}
            )


