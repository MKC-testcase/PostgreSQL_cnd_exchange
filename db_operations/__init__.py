#!/usr/bin/env python3
"""
By: Marcus Chan
Updated : 2020-12-24
Purpose: create a auto updating package when used
Libraries: gitPython, ([os,subprocess] should already be installed)
pip install gitPython <- install gitPython (assuming you are using pip to install)
"""

import os
import sys
import git
import subprocess

#this should install all required libraries for running this program
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psycopg2'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'unittest'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'time'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'csv'])
