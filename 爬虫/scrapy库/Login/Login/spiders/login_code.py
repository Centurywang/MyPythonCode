import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login_code'
    allowed_domains = ['yaozh.com']
    # 1 Login page--> Find the required parameters
    start_urls = ['https://www.yaozh.com/login']


    def parse(self, response):
        # 2.Login_code
        login_url = 'https://www.yaozh.com/login'
        formdata = {
            'username' : '15589771806',
                 'pwd' : 'wangshiji',
            'formhash' : response.xpath('//input[@id="formhash"]/@value').extract_first(),
             'backurl' : response.xpath('//input[@id="backurl"]/@value').extract_first(),
        }

        # post login request
        yield scrapy.FormRequest(
            login_url,
            formdata = formdata,
            callback=self.parse_login,
        )

    def parse_login(self,response):

        # scrapy take cookie request data

        # 3.Visit the target page
        member_url = 'https://www.yaozh.com/member/'
        yield scrapy.Request(
            member_url,
            callback=self.parse_member
        )

    def parse_member(self,response):

        with open('login_code.html','wb') as f:
            f.write(response.body)


