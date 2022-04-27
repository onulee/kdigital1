# https://fenderist.tistory.com/168  find 요소 설명
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time    # 대기시간 사용을 위해 import
import random  # 랜덤으로 input에 데이터 입력을 위해 import
import pyautogui


# 출력화면이 나타날때까지 대기하는 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# 브라우저 화면의 상태를 알려주는 라이브러리
from selenium.webdriver.support import expected_conditions as EC



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

# 항공권 도착 선택
# elements_by_class_name -> 모든class다 가져옴. [0],[1]...
browser.find_elements_by_class_name("select_code__d6PLz")[1].click()
time.sleep(2)
# 국내부분 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
time.sleep(2)
# 제주부분 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]/i[1]').click()


# 가는날/오는날 선택
# 가는날 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
# 24일 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[3]/button').click()
# 오는날 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(2)
# 25일 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[4]/button').click()

# 항공권 검색버튼 클릭
browser.find_element_by_class_name("searchBox_txt__3RoCw").click()


# 페이지 로딩완료까지 대기
# 브라우저 로딩후 10초대기, 화면에서 선택한 요소(xpath)가 있는지 체크
WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]')))
# time.sleep(10)

# 현재 높이 가져옴.
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 : ",prev_height)

# 무한반복
while True:
    # 자바스크립트 실행 - 스크롤을 아래방향으로 이동시켜줌.
    pyautogui.scroll(-prev_height)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 열리는 동안 대기
    time.sleep(2)
    # 변경후 높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height
    # 무한반복 끝
    print("현재 높이 : ",curr_height)
    
    
# # 무한반복
# while True:
#     # 자바스크립트 실행 - 스크롤을 아래방향으로 이동시켜줌.
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     # 페이지 열리는 동안 대기
#     time.sleep(2)
#     # 변경후 높이를 저장
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if prev_height == curr_height:
#         break # 스크롤 크기가 더 이상 변경이 없을시 종료
#     prev_height = curr_height
#     # 무한반복 끝
#     print("현재 높이 : ",curr_height)



# 현재 웹페이지 html소스를 가져옴.
page_html = browser.page_source
# BeautifulSoup html파싱
soup = BeautifulSoup(page_html,"lxml")

flights = soup.find_all("div",{"class":"domestic_Flight__sK0eA result"})
print("검색 개수 : ",len(flights))


# 금액 5만원 이하 항공권만 출력하고 저장하시오.
# csv파일 저장
# data = [column.get_text().strip() for column in columns] 
