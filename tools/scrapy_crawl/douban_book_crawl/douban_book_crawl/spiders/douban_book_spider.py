import json

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from urlparse import urljoin
from urlparse import urlparse
from urlparse import urlunparse
from posixpath import normpath

from douban_book_crawl.items import DoubanBookCrawlItem
 
def myjoin(base, url):
    url1 = urljoin(base, url)
    arr = urlparse(url1)
    path = normpath(arr[2])
    return urlunparse((arr.scheme, arr.netloc, path, arr.params, arr.query, arr.fragment))

class DoubanBookSpider(Spider):
	name = "douban_book_spider"
	allowed_domains = ["book.douban.com", "api.douban.com"]

	# start_urls = [
	# 	"https://book.douban.com/tag/",
	# ]

	# def start_requests(self):
	# 	yield Request("https://book.douban.com/tag/")

	start_urls = [
		"https://api.douban.com/v2/book/25862578",
	]

	def start_requests(self):
		yield Request("https://api.douban.com/v2/book/25862578", callback=self.parse_book)

	def check_book_in_library(self, response):
		item = response.meta['item']
		isbn = response.meta['isbn']
		print '\nchecking whether there is a printed books in SYSU library: ', response.url
		print '\nisbn is : ', isbn

		# check whether the isbn of the response meta is in the response.url page and 
		# whether the isbn of the response meta is the same as the the isbn in the response.url page
		sel = Selector(response)
		sysu_book_info_isbn = sel.xpath("/html/body/table[3]/tr[1]/td[1]/div[@class='tabcontent']/table/tr[2]/td[2]/a/text()").extract()
		if (sysu_book_info_isbn):
			sysu_isbn = sysu_book_info_isbn[0][:17].replace('-', '')
			print "sysu_book_info_isbn is : ", sysu_book_info_isbn[0], sysu_isbn
			if (isbn == sysu_isbn):
				print "True"
				item['book_isbn'] = response.url
				yield item
			else:
				print "False"
				return
		else:
			print "not found this book in sysu library"
			return
		

		#yield item

	def parse_book(self, response):
		print '\nparsing book_of_set_id: ', response.url

		sel = Selector(response)

		book_info_json = sel.xpath("/html/body/p/text()").extract()
		print '................................... START book_info_json ......................................\n'
		print book_info_json[0]
		print '................................... END book_info_json ......................................\n'
		# first check whether the book is in the sysu library
		book_info_decode = json.loads(book_info_json[0])
		print type(book_info_decode)
		book_isbn = book_info_decode["isbn13"]
		print "the isbn of this book is ", book_isbn

		item = DoubanBookCrawlItem()

		item['book_info'] = book_info_json[0].encode('utf-8')

		req_url = "http://202.116.64.108:8991/F/-?func=find-b&find_code=WRD&request=" + book_isbn + "&local_base=ZSU01"

		request = Request(req_url, callback=self.check_book_in_library, dont_filter=True)
		request.meta['item'] = item
		request.meta['isbn'] = book_isbn
		yield request

	def parse_list(self, response):
		print '\nparsing book_of_tag list: ', response.url

		base_url = "https://api.douban.com/v2/book"

		sel = Selector(response)

		book_urls = sel.xpath("//ul[@class='subject-list']/li[@class='subject-item']/div[@class='info']/h2/a/@href").extract()
		print '\n-------------------------------- Start Parsing Book In The Book_Url --------------------------------'

		for book_url in book_urls:
			#print 'book_url', book_url
			# select the book id
			book_id_temp = book_url[31:]
			book_id = book_id_temp[:-1]
			req_book_url = base_url + book_id
			print 'req_book_url', req_book_url

			yield Request(req_book_url, callback=self.parse_book)

		print '-------------------------------- Finish Parsing Book In The Book_Url --------------------------------\n'


	def parse_tag(self, response):
		print '\nparse_tag url is ', response.url

		for i in range(0, 99):
			req_url = response.url + "?start=" + str(20 * i) + "&type=T"
			print 'req_url in this page is ', req_url
			yield Request(req_url, callback=self.parse_list)


	def parse(self, response):
		base_url = "https://book.douban.com"
		print '\n################################ Start Parsing Tags In The Start_Url ################################'
		print 'parsing', response.url

		sel = Selector(response)

		# tag_urls = sel.xpath("//table[@class='tagCol']/tbody/tr/td/a/@href").extract()
		# print '################################ Finish Parsing Tags In The Start_Url ################################\n'

		# print '\n********************************* Start Parsing Book List In One Tag Page *********************************'
		# for tag_url in tag_urls:
		# 	print 'tag_url: ', myjoin(base_url, tag_url)
		# 	yield Request(myjoin(base_url, tag_url), headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}, callback=self.parse_tag)

		# print '********************************* Finish Parsing Book List In One Tag Page *********************************\n'
		
		tag_url = sel.xpath("//table[@class='tagCol']/tbody/tr/td/a/@href").extract()[0]
		print '################################ Finish Parsing Tags In The Start_Url ################################\n'

		print '\n********************************* Start Parsing Book List In One Tag Page *********************************'
		yield Request(base_url+tag_url, callback=self.parse_tag)

		print '********************************* Finish Parsing Book List In One Tag Page *********************************\n'


	