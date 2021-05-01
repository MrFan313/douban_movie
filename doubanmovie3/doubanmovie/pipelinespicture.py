# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        piclist = []
        piclist.append(item['pic'][0])
        #遍历海报地址
        for url in piclist:
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            if not os.path.exists("picture"):
                os.mkdir("picture")
            with open(os.path.join("picture",item["title"][0]+".jpg"),mode="wb")as file:
                file.write(response.content)
        return item