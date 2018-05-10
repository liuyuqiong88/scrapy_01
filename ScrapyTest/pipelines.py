# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ScrapytestPipeline(object):

    def open_spider(self,spider):
        self.file = open('itcast.json','w')

    def process_item(self, item, spider):

        dict_data = dict(item)
        str_data = json.dumps(dict_data,ensure_ascii=False)


        self.file.write(str_data + ",\n")

        return item

    def close_spider(self,spider):

        self.file.close()