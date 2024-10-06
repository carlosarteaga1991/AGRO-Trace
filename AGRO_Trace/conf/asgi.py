"""
Desarrollado por Carlos Arteaga, Honduras, Hackathon 2024 SpaceApps NASA
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

application = get_asgi_application()
