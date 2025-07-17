import scrapy
from hm9.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuoteItem()
            item['tags'] = quote.css("div.tags a.tag::text").getall()
            item['author'] = quote.css("small.author::text").get()
            item['quote'] = quote.css("span.text::text").get()
            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
