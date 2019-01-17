import scrapy
class Demoz_xpath(scrapy.Spider):
    name = 'books'

    start_urls =  [
        'http://www.kuaichuanwen.com/top/allvisit/',
        ]

    def parse(self, response):
        for b in response.xpath('//tr/td/a/'):
            title = b.xpath('./@title')
            link = b.xpath('./@href')
            yield {title : link}

        next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

