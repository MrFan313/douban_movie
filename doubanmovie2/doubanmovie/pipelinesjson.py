# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        #在项目管道中输出数据
        moviedict = {}
        moviedict["rank"] = item["rank"][0]
        moviedict["title"] = item["title"][0]
        with open("movie.json",mode="a",encoding="utf-8")as file:
            res = json.dumps(moviedict,ensure_ascii=False) + "\n"
            file.write(res)
            print(">>json文件写入成功")
        return item
