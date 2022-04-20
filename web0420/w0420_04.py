import requests
from bs4 import BeautifulSoup
import re
url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# 정규표현식을 가져고 검색
# items = soup.find_all("li",{"class":re.compile("^search")})
items = soup.find_all("li",{"class":"search-product"})
print("item 개수 : ",len(items))
for item in items:
    # 평점 4.5이상 , 상품평 100개이상, 1~5페이지까지, Apple뺄것
    
    
    
    
    # 평점 - 4.5이상만 출력
    rate = item.find("em",{"class":"rating"}).get_text() 
    # rate 문자를 실수형으로 형변환
    print(float(rate))  #문자를 실수로 변경후 크기 비교
    # 상품평 - 100개 이상만 출력
    rate_cnt = item.find("span",{"class":"rating-total-count"}).get_text() 
    # (150)-> 문자에서 첫번째부터 마지막 전까지 슬라이싱해서 가져옴.
    print(int(rate_cnt[1:-1]))  # rate_cnt>50

    # 제품명
    product_name = item.find("div",{"class":"name"}).get_text()
    # 제품명에 Apple 이라는 단어가 포함되어 있는지 확인
    # if "Apple" in product_name:
    #     print(item.find("div",{"class":"name"}).get_text())
    # 가격
    print(item.find("strong",{"class":"price-value"}).get_text())
    # 링크
    print("https://www.coupang.com/"+item.a["href"])
    print("-"*20)
