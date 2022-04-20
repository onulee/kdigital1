import requests
from bs4 import BeautifulSoup

url="http://corners.gmarket.co.kr/Bestsellers"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

t_div = soup.find("div",{"id":"topPlusItems"})
t2_div = t_div.find_next_sibling("div")
items = t2_div.find_all("li")
print(items[0].find("a",{"class":"itemname"}).get_text())
print(items[0].find("div",{"class":"s-price"}).strong.span.span.get_text())



print(len(items))

