# -*- coding: utf-8 -*-
import scrapy
from doubanmovie.items import DoubanmovieItem

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['douban.com']
    #指定起始页
    start_urls = ['https://movie.douban.com/top250']
    #解析数据
    def parse(self, response):
        #定位标签
        movie_item = response.xpath('//div[@class = "item"]')
        # print(movie_item)
        # #遍历数据
        for item in movie_item:
            # print(item)
            #xpath解析
            #创建采集对象
            movie = DoubanmovieItem()
            # 排名解析并赋值
            movie['rank'] = item.xpath('div[@class="pic"]/em/text()').extract()
            #电影名解析并赋值
            movie['title'] = item.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
            #返回生成器
            yield movie
        pass
