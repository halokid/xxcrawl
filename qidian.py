#coding=utf-8
'''
起点中文网月榜样前500名小说介绍
'''


import requests as req
import pandas as pd
from bs4 import BeautifulSoup as bs

pd.set_option('display.height',1000)
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)


class QidianHot:

  def __init__(self):
    pass

  def doCrawl(self):
    newsary = []
    for i in range(25):
      res=req.get('http://r.qidian.com/yuepiao?chn=-1&page=' + str(i))
      # print(res)
      soup = bs(res.text, 'html.parser')
      # print(soup)
      for news in soup.select('.rank-view-list li'):
        newsary.append({'title':news.select('a')[1].text,
                        'name':news.select('a')[2].text,
                        'style':news.select('a')[3].text,
                        'describe':news.select('p')[2].text,
                        'url':news.select('a')[0]['href']})

    # print(len(newsary))
    newsdf = pd.DataFrame(newsary)
    # print(newsdf)
    newsdf.to_excel('qidian_hot.xlsx')



if __name__ == '__main__':
  qh = QidianHot()
  qh.doCrawl()













