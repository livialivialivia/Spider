#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib2
import urllib

values = {"username":"liurongo910@163.com","password":"livia646588"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)

response = urllib2.urlopen(request)
print response.read()