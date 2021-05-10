=====
front-django-account
=====


Quick start
-----------

1. Add "front-django-account" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'front-django-account',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('accounts/front/', include('front-django-account.front_urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/account/front/login to participate in the poll.