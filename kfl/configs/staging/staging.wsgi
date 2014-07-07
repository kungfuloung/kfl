import os
import sys
import site

# Reordering the path code from http://code.google.com/p/modwsgi/wiki/VirtualEnvironments

# Remember original sys.path.
prev_sys_path = list(sys.path) 

site.addsitedir(os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../env")),
    "lib/python2.7/site-packages"
))

# Reorder sys.path so new directories at the front.
new_sys_path = [] 
for item in list(sys.path): 
    if item not in prev_sys_path: 
        new_sys_path.append(item) 
        sys.path.remove(item) 
sys.path[:0] = new_sys_path 

#redirecting stdout to stderr cuz geopy uses print statements
sys.stdout = sys.stderr

# put the Django project on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../apps")))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../lib")))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../ext")))

os.environ["DJANGO_SETTINGS_MODULE"] = "kfl.configs.staging.settings"

from django.core.handlers.wsgi import WSGIHandler
_application = WSGIHandler()

def application(environ, start_response):
    if environ.get("HTTP_X_FORWARDED_PROTOCOL") == 'https' or \
       environ.get("HTTP_X_FORWARDED_SSL") == 'on':
        environ['wsgi.url_scheme'] = "https"
    return _application(environ, start_response)
