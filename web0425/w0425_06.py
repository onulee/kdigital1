import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time    # 대기시간 사용을 위해 import
import random  # 랜덤으로 input에 데이터 입력을 위해 import

# 1. 크롬브라우저 생성
browser = webdriver.Chrome()

# 2. 페이지 이동
browser.get("https://www.naver.com/")

# 3. link_login클래스 클릭해서 다시 페이지 이동
browser.find_element_by_class_name("link_login").click()
    
# 4. 대기시간을 적용, 랜덤으로 1초~3초사이 시간을 대기함.    
time.sleep(random.uniform(1,3)) 

# 5. 자바스크립트 소스추가 및 자바스크립트 페이지 적용 
input_js = "document.getElementById('id').value='{id}';\
    document.getElementById('pw').value='{pw}'\
    ".format(id='onulee',pw='1111')
# 자바스크립트 적용, input데이터 삽입
browser.execute_script(input_js)   

# 6. 대기시간 적용
time.sleep(random.uniform(1,3)) 
    
# 7. 로그인 버튼 클릭    
browser.find_element_by_id("log.login").click()

time.sleep(20) 

# selenium방식으로 input데이터 입력

# # id input선택
# elem = browser.find_element_by_name("id")
# # input aa입력
# elem.send_keys("aa")
# # pw input선택
# elem = browser.find_element_by_name("pw")
# # pw input 11입력
# elem.send_keys("11")
# # enter키 입력
# elem.send_keys(Keys.ENTER)



