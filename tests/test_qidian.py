#-*- coding: utf-8 -*-

import io
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码


pd.set_option('display.height',1000)
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)



def testPageOne():
  res=requests.get('http://r.qidian.com/yuepiao?chn=-1&page=1')
  # print(res)
  soup = BeautifulSoup(res.text, 'html.parser')
  # print(soup)

  newsary = []
  for news in soup.select('.rank-view-list li'):
    # print(news)
    # print (news.select('a')[1].text, news.select('a')[2].text, news.select('a')[3].text,
    #        news.select('p')[1].text, news.select('p')[2].text, news.select('a')[0]['href'])
    newsary.append({'title':news.select('a')[1].text,
                    'name':news.select('a')[2].text,
                    'style':news.select('a')[3].text,
                    'describe':news.select('p')[2].text,
                    'url':news.select('a')[0]['href']})


  print(len(newsary))
  newsdf=pd.DataFrame(newsary)
  print(newsdf)


























