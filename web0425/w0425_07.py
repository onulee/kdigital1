from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time    # 대기시간 사용을 위해 import
import random  # 랜덤으로 input에 데이터 입력을 위해 import

# webdriver 크롬브라우저 변수 할당 
options = webdriver.ChromeOptions()
# 브라우저 종료되지 않게 하는 options
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

# 브라우저에서 url사이트를 실행
url = "https://flight.naver.com"
# 윈도우 창 최대화
browser.maximize_window()
browser.get(url)

# 항공권 출발 선택
browser.find_element_by_class_name("select_code__d6PLz").click()
time.sleep(2)
# 국내부분 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
time.sleep(2)
# 서울부분 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[1]/i[1]').click()






# page_url = browser.page_source

# soup = BeautifulSoup(page_url,"lxml")
# airs = soup.find_all("div",{"class":"domestic_Flight__sK0eA result"})
# print(len(airs))