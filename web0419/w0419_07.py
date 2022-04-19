import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
# url="https://comic.naver.com/index"
url="https://news.daum.net/"
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

newstrong = soup.find("strong",{"class":"tit_g"})
print(newstrong)
print("최신뉴스1 : ",newstrong.a.get_text().strip())
print("바로가기 링크 : ",newstrong.a["href"])





# atag = soup.find("a",{"id":"recommand_titleName_0"})
# ahref = atag["href"]
# print("1위 : ",atag.get_text())
# print("바로가기 링크 : ","https://comic.naver.com"+ahref)


