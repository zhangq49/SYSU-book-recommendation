#-*- coding: UTF-8 -*-
import urllib
import re
from bs4 import BeautifulSoup

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

def getBookInf(book):
    html = getHtml(book)
    soup = BeautifulSoup(html)
    imgUrl = soup.find('img', src = re.compile("^https://"))['src']
    

def getTagInf(tag):
    index = 0
    while(1):
        html = getHtml("https://www.douban.com/tag/" + tag.encode('UTF-8') + "?start=" + str(index*20))
        print "https://www.douban.com/tag/" + tag.encode('UTF-8') + "?start=" + str(index*20)
        index = index + 1
        soup = BeautifulSoup(html)
        for book in soup.find_all("a", href=re.compile("^https://book.douban.com/subject")):
            getBookInf(book['href'])
            break
        break

def searchTagList():
    tagList = getTagList()
    for tag in tagList:
        getInf("小说")

def test():
    tag = getTagList()[0]
    getTagInf(tag)


test()



