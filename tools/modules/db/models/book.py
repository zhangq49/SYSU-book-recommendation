# -*- coding: utf-8 -*-

class Book(object):
    """Model for Book
    
    The attribute {labels} is a list of string. eg. ['book', 'music', 'food']
    """
    def __init__(self, name, imgUrl,
      isbn='', author='', press='', doubanPoint=0, doubanRateSum=0,
      bookDescription='', authorDescription='', sysuLibUrl='',
      labels=[]):
        super(Book, self).__init__()
        # Majar infomations
        self.name = name
        self.imgUrl = imgUrl
        # More details
        self.isbn = isbn
        self.author = author
        self.press = press
        self.doubanPoint = doubanPoint
        self.doubanRateSum = doubanRateSum
        self.bookDescription = bookDescription
        self.authorDescription = authorDescription
        self.sysuLibUrl = sysuLibUrl
        #
        self.labels = labels
