import dotenv
import sys
import os

dotenv.load_dotenv()

from django.conf import settings

BASE_DIR = os.path.dirname(__file__)

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
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR,'pages'),
    TEMPLATES=[
        {
            'BACKEND':'django.template.backends.django.DjangoTemplates',
            'DIRS':['templates'],
            'APP_DIRS':True,
        }
    ],
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)