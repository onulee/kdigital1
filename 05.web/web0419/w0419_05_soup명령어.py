import requests
from bs4 import BeautifulSoup
url="https://comic.naver.com/index"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
    
# text를 lxml css파싱, beautifulSoup에서 html파싱해서 soup 가져옴.
soup = BeautifulSoup(res.text,"lxml") 
# print(soup)
print("title : ",soup.title)
print("title제목 : ",soup.title.get_text())
print("a : ",soup.a)
print("a attr : ",soup.a.attrs)
print("a attr href : ",soup.a["href"])
print("a text : ",soup.a.get_text())
# # print("div : ",soup.div)
# print("div : ",soup.div.attrs)
# print("div id : ",soup.div["id"])

print("div id=menu : ",soup.find("div",attrs={"id":"menu"}))
print("div id=menu : ",soup.find(attrs={"href":"menu"}))

