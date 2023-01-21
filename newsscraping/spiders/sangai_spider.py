import scrapy 

class SangaiSpider(scrapy.Spider):
    name = "mani_news"

    start_urls = [
        'https://www.thesangaiexpress.com/manipuri/Editorials.html'
    ]

    def parse(self, response):
        for href in response.css('div.category a::attr(href)').getall():
            yield response.follow(href, callback=self.parse)

        yield {
                'heading': response.css('div.heading_container h1::text').get(),
                'content': response.xpath('//*[@id="NewsComp-fjId-mQfS-GbEf-lvsG"]/div[5]/text()').getall(),
            }
        
      

