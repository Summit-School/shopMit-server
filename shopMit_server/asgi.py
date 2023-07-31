# RailwayApp/asgi.py

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopMit_server.settings.py')
application = get_asgi_application()
