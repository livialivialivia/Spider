#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib2

#response = urllib2.urlopen("http://www.baidu.com")
#print response.read()
#建议使用request对象,因为在构建请求时,还需要加入好多内容
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()