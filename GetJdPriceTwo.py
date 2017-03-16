#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import BeautifulSoup
import requests

url = 'https://list.jd.com/list.html?cat=737,794,798'
html = requests.get(url).content

soup = BeautifulSoup.BeautifulSoup(html,'lxml')

