import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
url="https://comic.naver.com/index"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
# 10개의 인기웹툰 ol태그 가져옴 ( li태그 10개 담겨져 있음 )
rankall = soup.find("ol",{"id":"realTimeRankFavorite"})
# 10개의 li태그를 리스트 형태로 반환
cartoons = rankall.find_all("li")
for i,cartoon in enumerate(cartoons):
    print("{:2d}위 : {}".format(i+1,cartoon.a.get_text()))
    print("바로가기 링크 : {}".format("https://comic.naver.com/"+cartoon.a["href"]))

# rank2 = soup.find("li",{"class":"rank02"})
# 현재기준 바로 다음 검색
# print(rank1.next_sibling.next_sibling.next_sibling.next_sibling)
# find_next_sibling 현재기준부터 li를 찾을때까지 검색
# print(rank1.find_next_sibling("li").find_next_sibling("li"))
# 현재기준 이전에서 li를 찾을때까지 검색
# print(rank2.find_previous_sibling("li"))


