#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import urllib2
values = {}
values['username'] = "liurongo910@163.com"
values['password'] = "livia646588"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url+"?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()