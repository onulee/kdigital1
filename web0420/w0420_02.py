import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=703846&weekday=tue"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find_all("td",{"class":"title"})
for i,cartoon in enumerate(cartoons):
    print("제목 : ",cartoon.a.get_text())
    cartoon_url = "https://comic.naver.com"+cartoon.a["href"]
    print("바로가기 링크 : ",cartoon_url)
    print("-"*20)
