#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import urllib2
import cookielib

filename = 'qqmailcookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({'u':'798817612','p':'livia646588'})
loginUrl = 'https://mail.qq.com/cgi-bin/loginpage'

result = opener.open(loginUrl,postdata)
cookie.save(ignore_discard = True,ignore_expires = True)

objecturl = 'https://mail.qq.com/cgi-bin/frame_html?sid=HFAh8QyNxFiTT2A4&r=07cf5f894813ba127a4f21ca1ec89f14'

results = opener.open(objecturl)
print results.read()