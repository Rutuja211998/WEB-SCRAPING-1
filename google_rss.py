"""
This file containing scarping for the google using beautiful soup and giving the lastest feed using rssfeed.
Author: Rutuja Tikhile.
Data:18/4/2020
"""
import scrapy


class GoogleRssSpider(scrapy.Spider):
    name = "google_rss"

    def start_requests(self):
        urls = [
            'https://www.blog.google/rss/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'title': post.xpath('title//text()').extract_first(),
                'link': post.xpath('link//text()').extract_first(),
                'pubDate': post.xpath('pubDate//text()').extract_first(),
            }