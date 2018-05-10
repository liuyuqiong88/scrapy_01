# -*- coding: utf-8 -*-
import scrapy
from ScrapyTest.items import ScrapytestItem


class ItcastTestSpider(scrapy.Spider):
    name = "itcast_test"
    allowed_domains = ["itcast.cn"]
    start_urls = (
        'http://www.itcast.cn/channel/teacher.shtml',
    )

    def parse(self, response):
        node_list = response.xpath('//div[@class="li_txt"]')
        print('&&&&&:', len(node_list))

        for note in node_list:

            item = ScrapytestItem()
            item['name'] = note.xpath('./h3/text()').extract()[0]
            item['title'] = note.xpath('./h4/text()').extract()[0]
            item['desc'] = note.xpath('./p/text()').extract()[0]


            yield item

