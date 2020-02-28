"""
WSGI config for tnainventory project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""


import os
14
15
from whitenoise.django import DjangoWhiteNoise
16
17
from django.core.wsgi import get_wsgi_application
18
19
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tnainventory.settings')
20
21
application = get_wsgi_application()
22
23
application = DjangoWhiteNoise(application)
