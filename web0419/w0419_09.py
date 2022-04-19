import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
url="https://comic.naver.com/webtoon/weekday"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
cul = soup.find("div",{"class":"col_inner"}).ul
cartoons = cul.find_all("li")
for cartoon in cartoons:
    print("")
