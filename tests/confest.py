import sys
import os

# Add the source directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configure pytest to find the tests in the source directory
pytest_plugins = [
    'django_webpage.tests',
]