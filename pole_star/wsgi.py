"""
WSGI config for pole_star project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pole_star.settings")

application = get_wsgi_application()
