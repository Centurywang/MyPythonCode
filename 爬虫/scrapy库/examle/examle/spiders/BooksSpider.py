import scrapy

class BooksSpider(scrapy.Spider):
    # 实现start_requests 方法，替代start_urls类属性
    def start_requests(self):
        yield scrapy.Request('http://books.toscrape.com/',
                             callback=self.parse_book,
                             headers={'User-Agent':'Mozilla/5.0'},
                             dont_filter=True
        )

    # 改用parse_book作为回调函数
    def parse_book(self,response):
        pass

