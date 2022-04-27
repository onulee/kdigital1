import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import re
import csv

# webdriver options 설정
options = webdriver.ChromeOptions()
# 브라우저 종료되지 않게 설정
options.add_experimental_option("detach", True)
# # 화면숨김
# options.headless = True
# # 화면 최대화
# options.add_argument("window-size=1920x1080")

# 브라우저 열기
browser = webdriver.Chrome(options=options)
# 화면 최대화
browser.maximize_window()

# csv파일 저장
filename = "yanolja.csv"
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
# ,분리해서 list타입으로 반환
title="숙소,평점,가격,링크".split(",")
# title csv에 저장
writer.writerow(title)

url="https://www.yanolja.com/"
browser.get(url)





# time.sleep(2)
# 검색클릭
browser.find_element_by_xpath('//*[@id="__next"]/section/header/div/a[2]').click()
time.sleep(2)

# 날짜 선택 부분
browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[2]/button[1]').click()
time.sleep(1)
# 입실날짜
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[6]').click()
# 퇴실날짜
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[7]').click()
# 확인클릭
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[4]/button').click()

# 검색창 제주리조트 입력
elem = browser.find_element_by_class_name('SearchInput_input__342U2')
elem.send_keys('제주리조트')
elem.send_keys(Keys.ENTER)

#화면이 나타날때까지 대기
WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[1]/main/div/section[2]/div/div/div[1]')))
# time.sleep(5)

#스크롤 내림
prev_height = browser.execute_script("return document.body.scrollHeight")
time.sleep(2)
while True:
    # browser.execute_script("window.scroll(0,document.body.scrollHeight)")
    # 마우스 중앙으로 이동
    pyautogui.moveTo(500,500)
    # 마우스 아래로 이동
    pyautogui.scroll(-prev_height)
    time.sleep(2)
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

# 화면 스크린샷
browser.get_screenshot_as_file("yanolja.jpg")
        
soup = BeautifulSoup(browser.page_source,"lxml")

# 숙소리스트
items = soup.find_all("div",{"class":"PlaceListItemText_container__fUIgA text-unit"})
for i,item in enumerate(items):
    title = item.find("strong",{"class":"PlaceListTitle_text__2511B small"}).get_text()
    # 평점이 없을시 제외
    if not item.find("span",{"class":"PlaceListScore_rating__3Glxf"}):
        continue
    
    rate = float(item.find("span",{"class":"PlaceListScore_rating__3Glxf"}).get_text())
    # 금액이 없을시 제외
    if item.find("span",{"class":"PlacePriceInfo_salePrice__28VZD"}).get_text()=="예약마감":
        continue
    price = item.find("span",{"class":"PlacePriceInfo_salePrice__28VZD"}).get_text()
    item_url = item.find("a",{"class":"common_clearfix__M6urU"})["href"]

    if rate < 4.0:
        continue
    
    item_url = "https://www.yanolja.com"+item_url
    # 출력부분
    print("숙소명 : ",title)
    print("평점 : ",rate)
    print("가격 : ",price)
    print("링크 : ",item_url)
    print("-"*50)

    # csv에 모든 숙소 저장
    data=[]
    data.append(title)
    data.append(rate)
    data.append(price)
    data.append(item_url)
    writer.writerow(data)

    # 파일저장
    img_item = item.find("div",{"class":"PlaceListImage_imageText__2XEMn"})["style"]
    # https로 시작하는 위치 반환
    temp = img_item.find("https://")
    img_item = img_item[temp:-3]
    print("파일 위치 : ",img_item)
    res_img = requests.get(img_item)
    with open("item_{}.jpg".format(i),"wb") as f:
        f.write(res_img.content)
f.close()
# print(soup.prettify())