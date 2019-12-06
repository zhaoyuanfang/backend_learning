#!/usr/bin/env python
import os
import sys
sys.path[0] = '../'
sys.path.append('../tmitter')
sys.path.append('../tmitter/utils')
sys.path.append('../tmitter/mvc')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
