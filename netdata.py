# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:05:50 2019

@author: duany
"""
''''
#调用库
import requests
#发送请求，抓取url
r = requests.get('https://book.douban.com/subject/33377952/comments/')
#查看状态码
r.status_code
#查看抓取信息
r.text

from bs4 import BeautifulSoup

markup = '<p class="title"><b>The Little Prince</b></p>'

soup = BeautifulSoup(markup, "lxml")
soup.b
type(soup.b)
'''
#源代码程序
import requests
from bs4 import BeautifulSoup
import re
#获取url
r = requests.get('https://book.douban.com/subject/33377952/comments/')
soup = BeautifulSoup(r.text, 'lxml')
#评论行的标签是span而不是p，属性是short，find_all返回一个列表
#寻找所解析内容要与原网页源代码相符
pattern = soup.find_all('span', 'short')
#迭代输出评论
for item in pattern:
    print(item.string)    
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating" title="力荐">')
p = re.findall(pattern_s, r.text)
#需要先定义sum的类型,否则出现TypeError错误
sum = 0
for star in p:
    sum += int(star)
print(sum)
