# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class RasterTypePipeline(object):
    def __init__(self):
        self.file1 = open('out1.txt', 'wb')
        self.file2 = open('out2.txt', 'wp')
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['flag'] != "Yes":

            long = item['long_name'][0].split('\n')[0]
            short = item['short_name'][0].split('\n')[0]

            if long in self.ids_seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                line1 = "'" + long + "': '" + short + "',\n"
                line2 = "'" + short + "': '" + long + "',\n"
                self.file1.write(line1)
                self.file2.write(line2)
                self.ids_seen.add(long)
                return item
        else:
            raise DropItem("Missing price in %s" % item)
