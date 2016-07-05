# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..')))
print(sys.path[0])


def main():
    from dbhelper import bowokTest
    from dbhelper import bookLabelTest

if __name__ == '__main__':
    main()


