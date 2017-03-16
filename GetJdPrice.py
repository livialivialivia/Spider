#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import BeautifulSoup
import lxml


res = urllib.urlopen("http://item.jd.com/3296817.html")

soup = BeautifulSoup.BeautifulSoup(res)

title = soup.find(attrs = {"class":"sku-name"})
print title.string
price = soup.find(attrs = {"class":"price J-p-3296817"})
print price.string
'''
Lists = soup.find(attrs = {"id":"plist"})
titles = Lists.findAll(attrs = {"class":"p-name"}).a.em
price = Lists.findAll(attrs = {"class":"J_price"}).i
for title in titles:
    print title.string'''


