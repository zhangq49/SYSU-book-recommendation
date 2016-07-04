# -*- coding: utf-8 -*-

class BookLabel(object):
    """Model for BookLabel"""
    def __init__(self, name, useCount):
        super(BookLabel, self).__init__()
        self.name = name
        self.useCount = useCount
