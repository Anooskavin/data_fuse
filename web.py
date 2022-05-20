from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import pandas as pd

req = Request("http://www.indiapress.org/")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))
top_10_news=[]
top_10_hits=[]
top_10_links=[]
news_lang_links=[]
news_lang_names=[]
for link in soup.findAll('b'):
  a=str(link)
  # print(a)
  if   '<font face="Verdana" size="2">'in a:
    top_10_news.append(a[33:33+ (a[33:].index('<'))])
  if "Hits)" in a:
    top_10_hits.append(int(a[5:-10]))
for i in links:
  s=str(i)
  # print(s)
  if  "news.php" in s:
    top_10_links.append(i)





print(top_10_news)
print(top_10_hits)
print(top_10_links)
print(news_lang_links)
print(news_lang_names)
print(news_lang_links)
a = pd.DataFrame()
a["top_10_news"]=top_10_news
a["top_10_hits"]=top_10_hits
a["top_10_links"]=top_10_links
# print(a)
a.to_excel("top10.xlsx") 

b = pd.DataFrame()
b ["news_lang_names"] = news_lang_names
b["news_lang_links"]=news_lang_links
b.to_excel("lang.xlsx")
