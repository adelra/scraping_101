from bs4 import BeautifulSoup
import urllib
from lxml import etree
from lxml import html
import requests


url = 'http://www.irna.ir/fa/page/260'
data = urllib.request.urlopen(url).read()

page = BeautifulSoup(data,'html.parser')
all_links = []
for link in page.findAll('a'):
       l = link.get('href')
       all_links.append("http://irna.ir/"+str(l))
for each in all_links:
    page = requests.get(each)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    content = tree.xpath('//*[(@id = "ctl00_ctl00_ContentPlaceHolder_ContentPlaceHolder_NewsContent4_BodyLabel")]')
    print (content)
