import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
url="https://comic.naver.com/webtoon/weekday"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
cul = soup.find("div",{"class":"col_inner"}).ul
cartoons = cul.find_all("li")
for i,cartoon in enumerate(cartoons):
    clink = cartoon.a["href"]
    ctxt = cartoon.find("a",{"class":"title"}).get_text()
    print("{:2d}위 : {}".format(i+1,ctxt))
    print("바로가기 링크 : {}".format("https://comic.naver.com"+clink))
