#! /usr/bin/env python
# _*_ coding: utf-8 _*_

# IP代理使用

import urllib2
import BeautifulSoup

#如何获取本机浏览器的user_agent ,在console中输入:navigator.userAgent
User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
header = {}
header['User-Agent'] = User_Agent

url = 'http://www.xicidaili.com/nn/1'
req = urllib2.Request(url,headers=header)
res = urllib2.urlopen(req).read()

soup = BeautifulSoup.BeautifulSoup(res)
ips = soup.findAll('tr')
f = open("proxy","w")

for x in range(1,len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\n"
    #print tds[1].contents[0]+"\t"+tds[2].contents[0]
    f.write(ip_temp)