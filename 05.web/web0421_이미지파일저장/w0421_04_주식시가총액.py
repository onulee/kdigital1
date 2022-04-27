from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import csv  #csv파일 라이브러리
import re

url="https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

# csv파일 저장
filename="시가총액1-200.csv"
# newline="" 자동enter키 생략
# 엑셀파일 한글인코딩방법 : utf-8-sig타입으로 저장
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

# 상단 제목 입력
# csv파일은 list타입 저장가능
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE"
# split함수 : 문자를 분기할 타입을 기준으로 list타입으로 변환
title = title.split("\t")
writer.writerow(title)

data_rows = soup.find("table",{"class":"type_2"}).tbody.find_all("tr")
# tr안에 td를 모두 가져오기 위해 for문 실행
for row in data_rows:
    # 각row마다 td를 가지고 옴.-list타입 1,13,13,13,13,13,1,1,1,13...
    columns = row.find_all("td")
    # td가 1개 인것은 skip, td가 13개 인것(데이터)만 가져옴.  
    if len(columns)<=1:
        continue 
    # td가 13개인것만 존재, 데이터 읽어오기
    # 엑셀파일,csv파일은 저장할때 list타입만 저장가능
    data=[]
    for column in columns: 
        data.append(column.get_text().strip())
      
    # 한줄 for문 사용    
    # data = [column.get_text().strip() for column in columns]    
        
    writer.writerow(data)
f.close()
