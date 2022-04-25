import requests
from bs4 import BeautifulSoup
url="http://www.naver.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# soup.prettify로 파일저장
with open("bbb.html",'w',encoding="utf-8") as f:
    f.write(soup.prettify())   # html 정렬해서 출력

# 파일 저장.
# with open("aaa.html","w",encoding="utf-8") as f:
#     f.write(res.text)