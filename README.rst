=====
front-django-account
=====


Quick start
-----------

1. Add "front-django-account" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'accounts',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('accounts/front/', include('accounts.front_urls')),
