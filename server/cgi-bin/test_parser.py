
import requests
import sys
from bs4 import BeautifulSoup as BS

r = requests.get("https://marketing.uz/brend-goda-2021/")
html = BS(r.content, "html.parser")
sys.stdout.reconfigure(encoding='utf-8')
for el in html.select(".votign-items > figure"):
  cap = el.select(".cap-content span")
  print(cap[0].text)