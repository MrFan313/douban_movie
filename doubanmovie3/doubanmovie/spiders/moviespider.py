# -*- coding: utf-8 -*-
import scrapy
from doubanmovie.items import DoubanmovieItem
import os
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
            #获取影评
            movie["quote"] = item.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()
            # 获取海报
            movie['pic'] = item.xpath('div[@class="pic"]/a/img/@src').extract()
            #返回生成器
            yield movie
        #深度采集
        #从当前页获取下一页链接
        next_page = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_page:
            choice = input("是否需要抓取下一页:(y/n)?n\n")
            if choice.lower() == 'y':
                #获取下一页地址
                next_url = "https://movie.douban.com/top250"+next_page[0]
                yield scrapy.Request(next_url,self.parse)
            else:
                os.path.exists(0)