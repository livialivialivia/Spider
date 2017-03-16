#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib
import json
import socket
socket.setdefaulttimeout(10)
proxys = []
proxys.append({"http":"http://114.239.0.220:808"})
proxys.append({"http":"http://180.117.113.229:8998"})
proxys.append({"http":"http://175.155.25.72:808"})
for id in range(0,5,1):
    try:
        url = "http://chanyouji.com/api/trips/"+`(352140+id)`+".json"
        res = urllib.urlopen(url,proxies=proxys[id%3]).read()
        res_json = json.loads(res)
        print res_json['name']
    except Exception,e:
        print e
        continue