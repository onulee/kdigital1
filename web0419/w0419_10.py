# 평균평점
# rate = (float(9.98)+float(9.97))/2
import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
url="https://comic.naver.com/webtoon/weekday"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find_all("td",{"class":"title"})
print(cartoons[0].a.get_text())