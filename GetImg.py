#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' %x)
        x += 1


html = getHtml("https://tieba.baidu.com/p/2460150866")

print getImg(html)