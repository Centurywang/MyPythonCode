import scrapy
from tutorial.items import TutorialItem
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [ "http://www.kuaichuanwen.com/top/allvisit/",
       ]

    def parse(self,response):
        title = response.xpath('//tr//td/a/text()').extract()
        link = response.xpath('//tr//td/a/@href').extract()
        for t,l in zip(title,link):
            item = TutorialItem()
            item['title'] = t
            item['link'] = l
            yield item


