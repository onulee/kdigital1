import requests
from bs4 import BeautifulSoup
import re
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

# 1페이지에서 5페이지까지 검색
for i in range(1,6):
    url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    # 정규표현식을 가져고 검색
    # items = soup.find_all("li",{"class":re.compile("^search")})
    items = soup.find_all("li",{"class":"search-product"})
    item_cnt=0
    print("item 개수 : ",len(items))
    for i,item in enumerate(items):
        if "search-product__ad-badge" in item["class"]:
            continue
        # 평점 4.5이상 , 상품평 100개이상, 1~5페이지까지, Apple제외
        # li - class search-product__ad-badge 들어가 있는 제품은 제외
        
        # 평점 - 4.5이상만 출력
        if not item.find("em",{"class":"rating"}):
            continue
        else:
            rate = float(item.find("em",{"class":"rating"}).get_text())
        # 상품평 - 100개 이상만 출력
        rate_cnt = item.find("span",{"class":"rating-total-count"}).get_text() 
        rate_cnt = int(rate_cnt[1:-1])
        # (150)-> 문자에서 첫번째부터 마지막 전까지 슬라이싱해서 가져옴.
        if rate<4.5 or rate_cnt< 200 : 
            continue

        # 제품명
        product_name = item.find("div",{"class":"name"}).get_text()
        print("제품명 : {} ".format(product_name))
        # 제품명에 Apple 이라는 단어가 포함되어 있는지 확인
        # if "Apple" in product_name:
        #     print(item.find("div",{"class":"name"}).get_text())
        # 가격
        print("금액 : ",item.find("strong",{"class":"price-value"}).get_text())
        # 평점
        print("평점 : ",rate)
        # 상품평
        print("상품평 : ",rate_cnt)
        # 링크
        print("https://www.coupang.com"+item.a["href"])
        print("-"*20)
        item_cnt += 1
    
print("검색 된 개수 : ",item_cnt)    
