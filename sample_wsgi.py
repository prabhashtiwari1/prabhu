import os
import sys

path= '/home/openatnet/prabhu/mobiloitte_smart_home_solutions'
if path not in sys.path:
	sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] =  "mobiloitte_smart_home_solutions.settings"

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler


application = StaticFilesHandler(get_wsgi_application())
