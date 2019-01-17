import scrapy
from meizitu.items import MeizituItem

class Select_Urls(scrapy.Spider):
    name = 'meizitu'
    start_urls = [
        'https://www.mzitu.com/xinggan/',
    ]

    def parse(self, response):
        title = response.xpath('//div[@class="postlist"]//li/a/text()').extract()
        link = response.xpath('//div[@class="postlist"]//li/a/@href').extract()

        for t,l in zip(title,link):
            item = MeizituItem()
            item[t] = l
            yield item

        next_page_url = response.xpath('//a[@class="next page-numbers"]/@href')
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))