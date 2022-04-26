import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import re
import csv

# csv파일 저장
filename="google_movie.csv"
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer =csv.writer(f)

# 상단제목 저장
title="제목 평점 가격".split(" ")
writer.writerow(title)

# webdriver옵션 가져오기
options = webdriver.ChromeOptions()
# 브라우저 종료되지 않게 하는 options
options.add_experimental_option("detach", True)
# 브라우저 열기
browser = webdriver.Chrome(options=options)
# 화면 최대화
browser.maximize_window()

url="https://play.google.com/store/movies/category/MOVIE"
# 국문페이지 설정
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
         "Accept-Language":"ko-KR,ko"
         }

# 사이트 열기
browser.get(url)
# 자바스크립트 실행
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # pyautogui.scroll(-prev_height)
    time.sleep(3)
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

# res = requests.get(url,headers=headers)
# res.raise_for_status()
# 현재페이지 html파싱
soup = BeautifulSoup(browser.page_source,"lxml")

# zuJxTd클래스 검색시 9개 검색이 됨. 마지막 9번째가 찾으려고 하는 것임.
m_section = soup.find_all("div",{"class":"zuJxTd"})
# print(len(movies))
# 리스트[8] 가족과 함께 보는 영화 콜렉션 가져옴.-listitem 20개 영화를 가져옴
m_articles = m_section[8].find_all("div",{"class":"ULeU3b neq64b"})

for m_article in m_articles:
    data=[]
    # 영화영상 링크
    movie_url = m_article.find("a",{"class":"Si6A0c ZD8Cqc"})["href"]
    # 영화이미지
    img_movie = m_article.find("img",{"class":"T75of etjhNc"})["src"]
    
    #----- 제목, 평점, 가격 정보
    movie = m_article.find("div",{"class":"hP61id"})
    # 제목
    title = movie.find("div",{"class":"Epkrse"}).get_text()
    # 평점
    rate = movie.find("div",{"class":"LrNMN"}).get_text()
    # 0-9까지 숫자와 .을 제외한 것은 모두 삭제처리
    rate = float(re.sub(r'[^0-9.]','',rate))
    # 가격
    price = movie.find("span",{"class":"VfPpfd VixbEe"}).span.get_text()
    price = int(re.sub(r'[^0-9]','',price))
    
    # 6천원 초과는 제외
    if price>6000:
        continue
    
    # csv파일 저장
    data.append(title)
    data.append(rate)
    data.append(price)
    writer.writerow(data)
    
    # 화면 출력
    print("제목 : ",title)
    print("평점 : ",rate)
    print("가격 : ",price)
    print("-"*50)

f.close()





