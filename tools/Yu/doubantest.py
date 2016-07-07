#-*- coding: UTF-8 -*-
import urllib

import urllib2
import re
from book import Book
from bs4 import BeautifulSoup
import bs4
import json
import random
import cookielib

bookUrlList = list()

head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
data = None

#Get a page through its url
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getHtml2(url):
    headers = {
        'User-Agent':head_user_agent[random.randrange(0,len(head_user_agent))],
        'Cookie':'viewed="25862578_26657570_26787931"; bid=6AKNIuCuCUM; gr_user_id=953140fa-8947-46bd-8f01-c6bbb186b931; __utma=30149280.1155223947.1467594905.1467594905.1467614162.2; __utmz=30149280.1467594905.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ll="118281"'
    }
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    html = response.read()
    return html

def getTagList():
    tagList = []
    html = getHtml2("https://book.douban.com/tag/?view=type")
    soup = BeautifulSoup(html)
    for tag in soup.find_all("a", href = re.compile("^/tag/.*")):
        tagList.append(tag.string.encode('UTF-8'))
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
    html = getHtml2(book)
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
    if not '出版社' in bookInf:
        bookInf['出版社'] = ''
    if not '作者' in bookInf:
        bookInf['作者'] = ''

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

def getBookFromJson(bookJson):
    print bookJson
    uid = -1
    print 'title: '
    print bookJson['title'].encode('UTF-8')
    name = bookJson['title'].encode('UTF-8')
    print 'image: '
    print bookJson['image'].encode('UTF-8')
    imgUrl = bookJson['image'].encode('UTF-8')
    print 'isbn: '
    print bookJson['isbn13'].encode('UTF-8')
    isbn = bookJson['isbn13'].encode('UTF-8')
    print 'author: '
    print bookJson['author']
    author = bookJson['author']
    print 'publisher'
    print bookJson['publisher'].encode('UTF-8')
    press = bookJson['publisher'].encode('UTF-8')
    print 'rating: '
    print bookJson['rating']['average']
    doubanPoint = bookJson['rating']['average']
    print 'rateSum: '
    print bookJson['rating']['numRaters']
    doubanRateSum = bookJson['rating']['numRaters']
    print 'Summary: '
    print bookJson['summary'].encode('UTF-8')
    bookDescription = bookJson['summary'].encode('UTF-8')
    print 'authorIntro: '
    print bookJson['author_intro'].encode('UTF-8')
    authorDescription = bookJson['author_intro'].encode('UTF-8')
    sysuLibUrl = ''
    return Book(uid, name, imgUrl,
      isbn, author, press, doubanPoint, doubanRateSum,
      bookDescription, authorDescription, sysuLibUrl)

def getBookJsonFromId(Id):
    bookStr = (getHtml2('https://api.douban.com/v2/book/' + str(Id)))
    return json.loads(bookStr)

def getIdFromUrl(url):
    sub = url.split('/')
    for x in sub[::-1]:
        if not x == '':
            return x

def getTagInf(tag):
    index = 0
    while(1):
        html = getHtml2("https://book.douban.com/tag/" + tag + "?start=" + str(index*20))
        index = index + 1
        print 'index:' + str(index) + '###########'
        soup = BeautifulSoup(html)
        if soup.find('div', id = 'subject_list').find('p').text.encode('UTF-8') == '没有找到符合条件的图书':
            print "Search done"
            break
        for book in soup.find_all("a", href=re.compile("^https://book.douban.com/subject"), class_ = "nbg"):
            print book['href']
            bookUrlList.append(book['href'])
            #getBookInf(book['href'])


##Search given tag and get book list
def searchTagList():
    tagList = getTagList()
    for tag in tagList:
        print '======================' + tag.encode('UTF-8') + '========================='
        getTagInf(tag)

#Just for test
def test():
    searchTagList()


#bookId = getIdFromUrl("https://api.douban.com/v2/book/25862578")
#bookJson = getBookJsonFromId(bookId)
#book = getBookFromJson(bookJson)
#printBook(book)



getTagInf('小说')
for bookUrl in bookUrlList:
    bookId = getIdFromUrl(bookUrl)
    print bookUrl
    bookJson = getBookJsonFromId(bookId)
    getBookFromJson(bookJson)
