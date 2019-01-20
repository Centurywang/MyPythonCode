import scrapy
from ..items import ExamleItem
class BookSpider(scrapy.Spider):
    # 每一个爬虫的唯一标识
    name = 'book'

    # 定义爬虫爬取的起始点，可以是多个
    start_urls = ['http://books.toscrape.com']

    def parse2(self,response):
        book = ExamleItem()
        book['ki'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]/@class').extract_first()
        book['Coding'] = response.xpath(
            '//*[@id="content_inner"]/article/table/tbody/tr[1]/td/font/font/text()').extract_first()
        book['numberRatings'] = response.xpath(
            '//*[@id="content_inner"]/article/table/tbody/tr[7]/td/font/font/text()').extract_first()
        book['numberStock'] = response.xpath(
            '//*[@id="content_inner"]/article/table/tbody/tr[6]/td/font/font/text()').extract_first()
        return book['ki'],book['Coding'],book['numberRatings'],book['numberStock']
    def parse(self, response):
        # 提取数据
        cont = response.xpath('//article[@class="product_pod"]')
        for i in cont:
            book = ExamleItem()
            book['name'] = i.xpath('.//h3/a/@title').extract_first()
            href = i.xpath('.//h3/a/@href').extract_first()
            href = response.urljoin(href)
            book['ki'],book['Coding'],book['numberRatings'],book['numberStock'] = scrapy.Request(href,callback=self.parse2)
            book['price'] = i.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
            yield book
        # 提取链接
        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_url:
            # 如果找到下一页的url，得到绝对路径，构造新的request对象
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url,callback=self.parse)
