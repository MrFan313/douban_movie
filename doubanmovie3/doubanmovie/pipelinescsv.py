# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
list1 = []
class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        rank = item["rank"][0]
        title = item["title"][0]
        dict1 = {}
        dict1["rank"] = rank
        dict1["title"] = title
        list1.append(dict1)
        with open('movie.csv',mode='w',encoding='utf-8',newline="")as file:
            write = csv.DictWriter(file,fieldnames = list1[0])
            #写入标题
            write.writeheader()
            #写入内容
            for i in list1:
                write.writerow(i)
            print("csv文件写入成功")
        return item
