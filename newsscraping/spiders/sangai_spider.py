import scrapy 

class SangaiSpider(scrapy.Spider):
    name = "mani_news"

    start_urls = [
        'https://www.thesangaiexpress.com/manipuri/Editorials.html',
        'https://www.thesangaiexpress.com/manipuri/State.html',
        'https://www.thesangaiexpress.com/manipuri/India.html',
        'https://www.thesangaiexpress.com/manipuri/World.html',
        'https://www.thesangaiexpress.com/manipuri//Encyc/2020/5/15/-K-W-l-J-K-A-W-J-R-A-J-t-R-J-l-K-J-J-K-K-.html',
        'https://www.thesangaiexpress.com/manipuri/General-Articles.html',
        'https://www.thesangaiexpress.com/manipuri/Sports-News.html',

    ]

    def parse(self, response):
        for href in response.css('div.category a::attr(href)').getall():
            yield response.follow(href, callback=self.parse)

        yield {
                'heading': response.css('div.heading_container h1::text').get(),
                'content': response.xpath('//*[@id="NewsComp-fjId-mQfS-GbEf-lvsG"]/div[5]/text()').getall(),
            }
        
      

