# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt
movielist = []
class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        rank = item['rank'][0]
        title = item['title'][0]
        dict1 = {}
        dict1["rank"] = rank
        dict1["title"] = title
        movielist.append(dict1)
        filepath = 'movie.xls'
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('第一页')
        header = [i for i in movielist[0]]
        for i in range(len(header)):
            sheet.write(0,i,header[i])
        data = []
        for a in  movielist:
            vlist = []
            for b in a.values():
                vlist.append(b)
            data.append(vlist)
        for i in range(1,len(movielist)+1):
            for j in range(len(header)):
                sheet.write(i,j,data[i-1][j])
        workbook.save(filepath)
        print(">>excel数据写入成功")
        return item