# -*- coding: utf-8 -*-

'''
This file shows some examples of dbhelpers.
'''

from modules.db.helper import bookLabel as labelHelper

def printLabels(labels):
    for label in labels:
        print label.name, label.useCount

def main():
    labels = labelHelper.getLabels(0, 2)
    printLabels(labels)
    print '-'
    labels = labelHelper.getLabels(1, 2)
    printLabels(labels)

main()
