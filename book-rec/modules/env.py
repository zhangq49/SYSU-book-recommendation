# -*- coding: utf-8 -*-

'''
If current working directory is /home/roger, we are on development mode.
'''
import sys
plist = sys.path[0].split('/')
if len(plist) > 2 and plist[1] == 'home' and plist[2] == 'roger':
    DEV = True
else:
    DEV = False