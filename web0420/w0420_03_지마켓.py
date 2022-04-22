from unittest import skip
import requests
from bs4 import BeautifulSoup

url="http://corners.gmarket.co.kr/Bestsellers"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

t_div = soup.find("div",{"id":"topPlusItems"})
t2_div = t_div.find_next_sibling("div")
items = t2_div.find_all("li")
for item in items:
    print(item.find("a",{"class":"itemname"}).get_text())
    print(item.find("div",{"class":"s-price"}).strong.span.span.get_text())
    item_icon = item.find("div",{"class":"icon"}).img
    print("test : **** ",item_icon)
    if item_icon:
        
        if item_icon["alt"] == "스마일배송":
            print("무료배송")
        else:
            print(item_icon.find_next_sibling("img"))
print(len(items))

