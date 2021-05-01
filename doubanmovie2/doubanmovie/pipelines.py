# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        #在项目管道中输出数据
        print("电影排名:{0}".format(item["rank"][0]))
        print("电影名称:{0}".format(item["title"][0]))
        return item
