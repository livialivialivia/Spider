#! /usr/bin/env python
# _*_ coding: utf-8 _*_

# 爬取豆瓣中某个页面书籍的所有书名

import urllib
import BeautifulSoup
import MySQLdb

res = urllib.urlopen("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
#获取目标页面,获取后,可使用 print res.read()打印出页面所有数据

soup = BeautifulSoup.BeautifulSoup(res)

book_div = soup.find(attrs = {"id":"book"})
book_a = book_div.findAll(attrs = {"class":"title"})

for book in book_a:
    print book.string
#输出a标签中的内容

"""
#若要将结果集放入数据库中,可以使用以下模块,这里的做法是错误的,只是显示连接DB是如何连接的
connection = MySQLdb.connect(host="127.0.0.1",user="root",passwd="mxj123",db="Spider",port=3306,charset="utf8")
cursor = connection.cursor()
sql = "insert into BookName value (%s), %(book.string)"
sql_res = cursor.execute(sql)
connection.commit()
cursor.close()
connection.close()
"""
