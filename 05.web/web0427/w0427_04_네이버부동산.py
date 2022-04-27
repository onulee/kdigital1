import time
from tkinter.tix import Tree
# 구글드라이버 selenium
from selenium import webdriver
# keys입력에 관한 메소드
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 출력화면이 나타날때까지 대기하는 메소드
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# 브라우저 화면의 상태를 알려주는 메소드
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

browser = webdriver.Chrome()
browser.maximize_window()
url='https://new.land.naver.com/complexes/2992?ms=37.5437166,126.9543368,17&a=APT:ABYG:JGC&e=RETAIL'
browser.get(url)

# 마우스 이동
pyautogui.moveTo(50,700)
# body스크롤 높이를 체크하는게 아니라, id=articleListArea 스크롤높이를 체크
pre_height = browser.execute_script("return articleListArea.scrollHeight")
time.sleep(2)
while True:
    browser.execute_script("window.scroll(0,articleListArea.scrollHeight)")
    # 마우스 휠로 스크롤을 내림
    pyautogui.scroll(-pre_height)
    time.sleep(2)
    
    # id가 articleListArea지역에서 스크롤 높이 확인
    curr_height = browser.execute_script("return articleListArea.scrollHeight")
    if curr_height == pre_height:
        break

    pre_height = curr_height
    
# 문자소스 html파싱
soup = BeautifulSoup(browser.page_source,"lxml")
# 왼쪽 매물물건지역 html정보
house = soup.find("div",{"id":"articleListArea"})
# 매물물건 리스트 가져오기
items = house.find_all("div",{"class":"item false"})

count = 0  #50번째 리스트 찾는 변수

for item in items:
    # 매매 물건인지 확인
    if item.find("span",{"class":"type"})!="매매":
        continue
    else: # 타입이 매매인 경우
        count += 1
    
    if count==50 : # 매매물건이 50번째일때 출력 
        print(item.find("span",{"class":"text"}))
        print(item.find("span",{"class":"type"}))  # 매매,전세,월세
        print(item.find("span",{"class":"price"}))
        print(item.find("strong",{"class":"type"}))
        print(item.find("span",{"class":"spec"}))
        print("전체물건 : ",len(items))
        break
    
# print(soup.prettify())