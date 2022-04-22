# 평균평점
# rate = (float(9.98)+float(9.97))/2
import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
all_rate = 0  #전체 평균변수

# 전체 페이지 for문
page_count=5
for i in range(1,page_count+1):
    url="https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu&page="+str(i)
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")
    
    web_table = soup.find("table",{"class":"viewList"})
    cartoons = web_table.find_all("tr")
    for i,cartoon in enumerate(cartoons):
        car_title = cartoon.find("td",{"class":"title"})
        if not car_title:  #글자가 없을때 false로 인식
            continue
        car_rate = cartoon.find("div",{"class":"rating_type"})
        temp_rate = car_rate.strong.get_text()
        all_rate += float(temp_rate)
        car_date = cartoon.find("td",{"class":"num"})
        print("제목 : ",car_title.a.get_text())   # 제목
        print("평점 : ",temp_rate)   # 평점
        print("날짜 : ",car_date.get_text())   # 날짜
        print("-"*20)
    
print("전체평균 : {:.2f}".format(all_rate/((len(cartoons)-1)*page_count)))    
    