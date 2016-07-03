# -*- coding: utf-8 -*-

class Book(object):
    """Model for Book"""
    def __init__(self, uid, name, imgUrl,
      isbn=None):
        super(Book, self).__init__()
        # Majar infomations
        self.uid = uid
        self.name = name
        self.imgUrl = imgUrl
        # More details
        self.isbn = isbn
