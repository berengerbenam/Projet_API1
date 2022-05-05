import sys
#sys.path.insert(0'/var/www/html/API1/API')
sys.path.append('/var/www/html/API1/API')
sys.stdout=sys.stderr
from api1 import app as application
