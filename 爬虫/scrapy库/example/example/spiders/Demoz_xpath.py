import scrapy
from ..items import ExampleItem

class BookSpider(scrapy.Spider):
    # 每一个爬虫的唯一标识
    name = 'book'

    # 定义爬虫爬取的起始点，可以是多个
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        # 提取数据
        cont = response.xpath('//article[@class="product_pod"]')
        for i in cont:
            book = ExampleItem()
            book['title'] = response.xpath('//h3/a/@title').extract_first()
            book['price'] = response.xpath('//div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
            yield book
        # 提取链接
        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_url:
            # 如果找到下一页的url，得到绝对路径，构造新的request对象
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url,callback=self.parse)
