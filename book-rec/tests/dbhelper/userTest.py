# -*- coding: utf-8 -*-

'''
This file shows some examples of dbhelpers.
'''

from modules.db.helper import user as userHelper

def main():
    userHelper.saveUser('aNewUser')

main()