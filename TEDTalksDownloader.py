import requests
from bs4 import BeautifulSoup
import re
import sys

if len(sys.argv)>1:
    url=sys.argv[1]

r=requests.get(url)
print("download starting...")
soup=BeautifulSoup(r.content,features="lxml")

for val in soup.find_all("script"):
    if(re.search("talkPage.init",str(val))) is not None:
        result=str(val)