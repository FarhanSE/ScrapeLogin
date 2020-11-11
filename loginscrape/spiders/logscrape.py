import scrapy
from scrapy.http import FormRequest
from ..items import LoginscrapeItem

class log(scrapy.Spider):
    name = 'login'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        
        crf_token = response.css('form input::attr(value)').extract()
        return FormRequest.from_response(response, formdata={
            'scrf_token':crf_token,
            'username': 'farhanbhn2222@gmail.com',
            'password':'datadas'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        items = LoginscrapeItem()
        all_quotes = response.css('div.quote')
        for q in all_quotes:
            title = q.css('span.text::text').extract()
            author = q.css('.author::text').extract()
            tags = q.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items 

