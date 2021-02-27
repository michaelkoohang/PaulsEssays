
import requests 
from bs4 import BeautifulSoup
from markdownify import markdownify as md

res = requests.get('http://paulgraham.com/articles.html')
soup = BeautifulSoup(res.content, "html.parser")
ignore = ["index.html", "https://sep.yimg.com/ty/cdn/paulgraham/acl1.txt?t=1614381162&", "https://sep.yimg.com/ty/cdn/paulgraham/acl2.txt?t=1614381162&"]

def parse_article(url):
  download = requests.get(url)
  soup = BeautifulSoup(download.content, "html.parser")
  file = open("./articles/" + url[22:-6] + ".md", "w")
  article = soup.find_all('table')[0]
  title = ''
  for img in article.find_all('img'):
    try:
      title = img['alt']
    except:
      print("ERR")
  file.write(title + "\n\n")
  file.write(md(str(article.find_all('font')[0])))
  file.close()

for link in soup.find_all('a'):
  href = link['href'].strip()
  print(href)
  if href not in ignore:
    parse_article('http://paulgraham.com/' + href)
