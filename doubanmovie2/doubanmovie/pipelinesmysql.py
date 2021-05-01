# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        #建立连接
        con = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='db_movie')
        #判断连接状态
        if con:
            print(">>数据库连接成功!")
        else:
            print(">>数据库连接失败!")
        #2,获取游标对象
        cur = con.cursor()
        # print(cur)
        #执行sql语句
        #处理异常
        try:
            res = cur.execute("insert into tb_movie values(id,'%d','%s')" %(int(item['rank'][0]),item['title'][0]))
            con.commit()
            print('>>事物提交成功!')
        except:
            con.rollback()
            print(">>事物回退成功!")
        cur.close()
        con.close()
        return item
