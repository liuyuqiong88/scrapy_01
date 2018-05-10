# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.com"]
    start_urls = (
        'http://www.itcast.com/',
    )

    def parse(self, response):


        pass
