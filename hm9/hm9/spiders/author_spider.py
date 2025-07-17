import scrapy
from hm9.items import AuthorItem

class AuthorSpider(scrapy.Spider):
    name = "authors"
    start_urls = ['http://quotes.toscrape.com']

    visited_authors = set()

    def parse(self, response):
        authors = response.css("div.quote a[href^='/author/']::attr(href)").getall()
        for author_url in authors:
            full_url = response.urljoin(author_url)
            if full_url not in self.visited_authors:
                self.visited_authors.add(full_url)
                yield response.follow(full_url, self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        item = AuthorItem()
        item['fullname'] = response.css("h3.author-title::text").get().strip()
        item['born_date'] = response.css("span.author-born-date::text").get().strip()
        item['born_location'] = response.css("span.author-born-location::text").get().strip()
        item['description'] = response.css("div.author-description::text").get().strip()
        yield item
