import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

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

movies = soup.find_all("div",{"class":"zuJxTd"})
# print(movies)
print(len(movies))

sec_movie = movies[8].find("div",{"class":"ULeU3b neq64b"})
print("-"*50)
print("1개 파일 : ",sec_movie.find("div",{"class":"hP61id"}))






