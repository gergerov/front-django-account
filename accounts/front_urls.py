from django.conf.urls import url
from django.urls import path
from accounts.front_views.front_login_views import LoginView
from accounts.front_views.front_registration_views import RegistrationView
from accounts.front_views.front_logout_view import LogoutView
from accounts.front_views.front_reset_password import ResetPasswordView
from accounts.front_views.front_reset_password_sended import ResetPasswordSendedView
from accounts.front_views.front_registration_success import RegistrationSuccess
from accounts.front_views.front_confirmation_reset_password import ConfirmationResetPassword
from accounts.front_views.front_reset_password_success import ResetPasswordSuccess
from accounts.front_views.front_confirmation_registration import ConfirmationRegistration
from accounts.front_views.front_confirmation_registration_success import ConfirmationRegistrationSuccess


urlpatterns = [

    url(
        r'^registration$'
        , view=RegistrationView.as_view()
        , name="front_registration"
    ),

    url(
        r'^registration_success$'
        , view=RegistrationSuccess.as_view()
        , name="front_registration_success"
    ),

    url(
        r'^login$'
        , view=LoginView.as_view()
        , name="front_login"
    ),

    url(
        r'^logout$'
        , view=LogoutView.as_view()
        , name="logout"
    ),

    url(
        r'^reset_password$'
        , view=ResetPasswordView.as_view()
        , name="front_reset_password"
    ),

    url(
        r'^reset_password_sended$'
        , view=ResetPasswordSendedView.as_view()
        , name="front_reset_password_sended"
    ),

    url(
        r'^confirmation_reset_password'
        , view=ConfirmationResetPassword.as_view()
        , name="front_confirmation_reset_password"
    ),

    url(
        r'^reset_password_success'
        , view=ResetPasswordSuccess.as_view()
        , name="front_reset_password_success"
    ),

    url(
        r'^confirmation_registration/$'
        , view=ConfirmationRegistration.as_view()
        , name="front_confirmation_registration"
    ),

    url(
        r'^confirmation_registration_success$'
        , view=ConfirmationRegistrationSuccess.as_view()
        , name="front_confirmation_registration_success"
    ),

]