from crispy_forms.layout import Layout, Fieldset, HTML


forgot_password_link = HTML(
    '<div class="row p-1 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1" >'
    '<a class="btn btn-warning btn-block" '
    'href="{% url "front_reset_password" %}">Forgot password?</a>'
    '</div>'
)

registration_link = HTML(
    '<div class="row p-1 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1" >'
    '<a class="btn btn-info btn-block" '
    'href="{% url "front_registration" %}">No account?</a>'
    '</div>'
)

home_link = HTML(
    '<div class="row p-1 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1" >'
    '<a class="btn btn-light btn-block" '
    'href="/">Home</a>'
    '</div>'
)

login_submit = HTML(
    '<div class="row p-1 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1" >'
    '<input type="submit" '
    'name="submit" value="Login" '
    'class="btn btn-primary btn-block" '
    'id="submit-id-submit">'
    '</div>'
)

login_link = HTML(
    '<div class="row p-1 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1" >'
    '<a class="btn btn-success btn-block" '
    'href="{%url "front_login" %}" %}>Already registered?</a>'
    '</div>'
)

registration_submit = HTML(
    '<div class="row p-1 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1" >'
    '<input type="submit" '
    'name="submit" '
    'value="Register" '
    'class="btn btn-primary btn-block" '
    'id="submit-id-submit">'
    '</div>'
)

send_reset_password_link = HTML(
    '<div class="row p-1 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1" >'
    '<input type="submit" '
         'name="submit" '
         'value="Send instructions" '
         'class="btn btn-primary btn-block" '
         'id="submit-id-submit">'
    '</div>'
)

accept_new_password = HTML(
    '<div class="row p-1 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1" >'
    '<input type="submit" '
         'name="submit" '
         'value="accept new password" '
         'class="btn btn-primary btn-block" '
         'id="submit-id-submit">'
    '</div>'
)

accept_registration = HTML(
    '<div class="row p-1 m-1 p-1 t-1 b-1 l-1 r-1 x-1 y-1" >'
    '<input type="submit" '
         'name="submit" '
         'value="accept registration" '
         'class="btn btn-primary btn-block" '
         'id="submit-id-submit">'
    '</div>'
)