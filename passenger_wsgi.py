import sys
import os

# Set the Python path for your application
sys.path.append(os.getcwd())
sys.path.append('/home/dh_985r5b/ams.webinfinitesolutions.com')

# Set the environment variable to inform Django about the production environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'Employee.settings'
