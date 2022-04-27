from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re

url="http://browse.auction.co.kr/search?keyword=tv&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=tv&acode=SRP_SU_0100&arraycategory=&encKeyword=tv"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

div1 = soup.find("div",{"id":"section--inner_content_body_container"})
items = div1.find_all("div",{"class":"itemcard"})
for i,item in enumerate(items):
    # 제목
    title = item.find("span",{"class":"text--title"}).get_text()
    # 가격
    price = item.find("strong",{"text--price_seller"}).get_text()
    # 가격 replace ,를 제거 -> int형변환
    price = int(price.replace(",",""))
    # 평점
    temp_rate = item.find("div",{"class":"seller_awards"})
    # 후기
    if item.find("span",{"class":"text--buycnt"}):
        buy_cnt = item.find("span",{"class":"text--buycnt"}).get_text()
        # 구매 라는 글자 삭제를 위한 re.sub()함수 실행
        # 0-9까지의 숫자가 아니면 삭제처리
        buy_cnt = int(re.sub(r'[^0-9]','',buy_cnt) )
    else:
        continue    
    
    if temp_rate: #평점이 없는 경우
        rate = temp_rate["title"]
        rate = float(re.sub(r'[^0-9.]','',rate))  
        # sub() 정규표현식을 가지고 해당되는 문자를 대체해서 변경함.
        # re.sub('r[정규표현식]','대체할문자',해당변수)
        if rate<4.5 and buy_cnt<100:
            continue
    else:
        continue
    
    print("{}.{}".format(i+1,title))
    print("가격 : ",price)     
    print("평점 : ",rate)
    print("후기 : ",buy_cnt)
    print("-"*50)
    

