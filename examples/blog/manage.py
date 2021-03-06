#!/usr/bin/env python
import imp

from django.core.management import execute_manager


# lamo cheat to make work a little easier. Don't do this in other places
import sys
import os
sys.path.insert(0, os.path.abspath('../..'))
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

if __name__ == "__main__":
    execute_manager(settings)
