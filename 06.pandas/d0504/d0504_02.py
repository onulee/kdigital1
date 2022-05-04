import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# webdriver옵션 가져오기
options = webdriver.ChromeOptions()
# 브라우저 종료되지 않게 하는 options
options.add_experimental_option("detach", True)
# User-Agent설정, 설정하지 않을시 HeadlessChrome 표시 됨.- 차단 당할수 있음 
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")

browser = webdriver.Chrome(options=options)

url="https://www.coupang.com/"
browser.get(url)
time.sleep(3)
# 자바스크립트 실행
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
browser.execute_script("window.scrollTo(0,300)")
time.sleep(2)
browser.execute_script("window.scrollTo(301,600)")
time.sleep(2)
browser.execute_script("window.scrollTo(600,1000)")
time.sleep(2)
browser.execute_script("window.scrollTo(1000,1500)")
time.sleep(2)
browser.execute_script("window.scrollTo(1500,document.body.scrollHeight)")
time.sleep(5)
# scroll(+):위쪽으로 이동, scroll(-):아래로 이동
# # 마우스 중앙으로 이동
# pyautogui.moveTo(500,500)
# # 마우스 아래로 이동
# pyautogui.scroll(-prev_height)


page_url = browser.page_source

# selenium으로 html소스 가져오기
soup = BeautifulSoup(page_url,"lxml")
# //*[@id="categoryBest_digital"]/dl[1]/dt/a/span

print(soup.find("div",{"id":"categoryBest_digital"}))

