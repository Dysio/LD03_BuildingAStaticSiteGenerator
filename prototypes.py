import dotenv
import sys
import os

dotenv.load_dotenv()

from django.conf import settings


settings.configure(
    DEBUG=os.environ.get("DEBUG"),
    SECRET_KEY = os.environ.get("SECRET_KEY"),
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    STATIC_URL='/static/',
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)