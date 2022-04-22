from unittest import skip
import requests
from bs4 import BeautifulSoup
import re

url="https://www.goodchoice.kr/product/result?keyword=%EC%98%A4%EC%85%98%EB%B7%B0"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

# 정규표현식
# items = soup.find_all("li",{"class":re.compile("^list_4")})
items = soup.find_all("li",{"class":"list_4"})
count=1
for i,item in enumerate(items):
    item_url = item.find("a")["href"]
    name = item.find("img",{"class":"lazy"})["alt"]
    
    if item.find("div",{"class":"name"}).find("div",{"class":"badge"}):
        name2 = item.find("div",{"class":"name"}).find("div",{"class":"badge"}).next_sibling
    else:
        name2 = item.find("div",{"class":"name"}).find("strong").get_text()
            
    name2 = name2.strip()
    rate = item.find("p",{"class":"score"}).span.em.get_text()
    rate = float(rate)
    # span태그 다음요소 선택, 좌우공백제거
    rate_cnt = item.find("p",{"class":"score"}).span.next_sibling.strip()
    # (184) -> 첫번째자리에서 마지막앞자리까지 슬라이싱 184
    rate_cnt = int(rate_cnt[1:-1])
    
    if rate<9.0 or rate_cnt<100:
        continue
    
    print("{}. 숙소명 : {}".format(count,name))
    print("{}. 숙소명2 : {}".format(count,name2))
    print("평점 : ",rate)
    print("상품평:",rate_cnt)
    print("바로가기 링크 : ",item_url)
    print("-"*20)
    count += 1
    
    





