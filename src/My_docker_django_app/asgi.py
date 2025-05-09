"""
ASGI config for my_docker_django_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import My_docker_django_app


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_docker_django_app.settings')
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

application = get_asgi_application()
