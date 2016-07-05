#-*- coding: UTF-8 -*-
import urllib
import re
from book import Book
from bs4 import BeautifulSoup
import bs4

#Get a page through its url
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getTagList():
    tagList = []
    html = getHtml("https://book.douban.com/tag/?view=type")
    soup = BeautifulSoup(html)
    for tag in soup.find_all("a", href = re.compile("^/tag/.*")):
        tagList.append(tag.string)
    return tagList

def printList(l):
    for sub in l:
        print sub
        print type(sub)

def printBook(bookItem):
    print '#############################'
    print 'uid:' + str(bookItem.uid)
    print 'name :' + str(bookItem.name)
    print 'imgUrl:' + str(bookItem.imgUrl) 
    print 'isbn:' + str(bookItem.isbn)
    print 'author:' + str(bookItem.author) 
    print 'press:' + str(bookItem.press)
    print 'doubanPoint:' + str(bookItem.doubanPoint)
    print 'sdoubanRateSum:' + str(bookItem.doubanRateSum)
    print 'bookDesciption:' + str(bookItem.bookDesciption)
    print 'authorDesciption:' + str(bookItem.authorDesciption)
    print 'sysuLibUrl:' + str(bookItem.sysuLibUrl)
    print '#############################'

def getTextList(content):
    textList = list()
    if isinstance(content, bs4.element.NavigableString):
        if (content.strip() == '' or content.strip() == ':'):
            return list()
        else:
            if content.strip()[-1] == ':':
                textList.append(content.strip()[:-1].encode('UTF-8'))
            else:
                textList.append(content.strip().encode('UTF-8'))
            return textList
    for sub in content.contents:
        textList.extend(getTextList(sub))
    return textList

def getBookInf(book):
    html = getHtml(book)
    soup = BeautifulSoup(html)
    imgUrl = soup.find('img', src = re.compile("^https://"))['src']

    inf = soup.find('div', id = 'info')
    textList = getTextList(inf)

    bookInf = {}
    for y in range(0, len(textList), 2):
        bookInf[textList[y]] = textList[y+1]
    
    bookInf['书名'] = soup.find('span', property = 'v:itemreviewed').text.strip().encode('UTF-8')
    bookInf['imgUrl'] = imgUrl.encode('UTF-8')
    if soup.find('strong').text.strip().encode('UTF-8') == '':
        bookInf['豆瓣评分'] = '0'
        bookInf['评分人数'] = '0'
    else:
        bookInf['豆瓣评分'] = soup.find('strong').text.strip().encode('UTF-8')
        bookInf['评分人数'] = soup.find('span', property = 'v:votes').text.strip().encode('UTF-8')
    
    intro = soup.find_all('div', class_ = 'intro')
    if len(intro) > 0:
        bookInf['内容简介'] = intro[0].text.strip().encode('UTF-8')
    else:
        bookInf['内容简介'] = ''
    if len(intro) > 1:
        bookInf['作者简介'] = intro[1].text.strip().encode('UTF-8')
    else:
        bookInf['作者简介'] = ''
    
    if not 'ISBN' in bookInf:
        return

    bookItem = Book(uid = -1,
                    name = bookInf['书名'],
                    imgUrl = bookInf['imgUrl'],
                    isbn = bookInf['ISBN'],
                    author = bookInf['作者'],
                    press = bookInf['出版社'],
                    doubanPoint = bookInf['豆瓣评分'],
                    doubanRateSum = bookInf['评分人数'],
                    bookDesciption = bookInf['内容简介'],
                    authorDesciption = bookInf['作者简介'],
                    sysuLibUrl='')
    printBook(bookItem)
    
def getTagInf(tag):
    index = 0
    while(1):
        html = getHtml("https://book.douban.com/tag/" + tag.encode('UTF-8') + "?start=" + str(index*20))
        index = index + 1
        print 'index:' + str(index) + '###########'
        #print ("https://book.douban.com/tag/" + tag.encode('UTF-8') + "?start=" + str(index*20))
        soup = BeautifulSoup(html)
        x = 0
        for book in soup.find_all("a", href=re.compile("^https://book.douban.com/subject"), class_ = "nbg"):
            if x % 2 == 0:
                print book['href']
                getBookInf(book['href'])
            x = x + 1

def searchTagList():
    tagList = getTagList()
    for tag in tagList:
        getInf("小说")

def test():
    tag = getTagList()[0]
    getTagInf(tag)


test()




