#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from useragent import pcualist
from useragent import wapualist



import requests
import json
  
url1 = 'http://www.baidu.com/'#登陆地址
url2 = "http://jiuxian.com/"#需要登陆才能访问的地址
data={"user":"user","password":"pass"}
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }
res1 = requests.post(url1, data=data, headers=headers)
res2 = requests.get(url2, cookies=res1.cookies, headers=headers)

print res2.content#获得二进制响应内容
print res2.raw#获得原始响应内容,需要stream=True
print res2.raw.read(50)
print type(res2.text)#返回解码成unicode的内容
print res2.url
print res2.history#追踪重定向

print res2.headers
print res2.headers['Content-Type']
print res2.headers.get('content-type')
print res2.json#讲返回内容编码为json
print res2.encoding#返回内容编码
print res2.status_code#返回http状态码
print res2.raise_for_status()#返回错误状态码