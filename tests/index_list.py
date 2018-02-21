#-*- coding: utf-8 -*-

import io
import sys
import requests
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

res=requests.get('http://r.qidian.com/yuepiao?chn=-1&page=1')
# print(res)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)

for news in soup.select('.rank-view-list li'):
  # print(news)
  print (news.select('a')[1].text, news.select('a')[2].text, news.select('a')[3].text, news.select('p')[1].text, news.select('p')[2].text, news.select('a')[0]['href'])

