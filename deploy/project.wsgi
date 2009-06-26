import os
import sys

# redirect sys.stdout to sys.stderr for bad libraries that use
# print statements for optional import exceptions.
sys.stdout = sys.stderr

from os.path import abspath, dirname, join
from site import addsitedir

sys.path.insert(0, abspath(join(dirname(__file__), "../../")))
sys.path.insert(0, abspath(join(dirname(__file__), "../")))

from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "alertante.settings"


from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
