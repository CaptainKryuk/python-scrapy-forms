import scrapy

class FormsSpider(scrapy.Spider):
    name = "forms"
    start_urls = [
        'necessary_url'
    ]

    def parse(self, response):
        print('Processing...' + response.url)
        if 'urlpart' in response.url():
            yield {
                'forms': response.xpath('//form[@method="post"]').extract()
            }

        next_pages = response.xpath('//a/@href').extract()
        for page in next_pages:
            if page is not None:
                yield scrapy.Request(response.urljoin(page))
