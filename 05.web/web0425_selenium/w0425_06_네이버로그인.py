import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time    # 대기시간 사용을 위해 import
import random  # 랜덤으로 input에 데이터 입력을 위해 import

# 1. 크롬브라우저 생성
# webdriver옵션 가져오기
options = webdriver.ChromeOptions()
# 브라우저 종료되지 않게 하는 options
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

# 2. 페이지 이동
browser.get("https://www.naver.com/")

# 3. link_login클래스 클릭해서 다시 페이지 이동
browser.find_element_by_class_name("link_login").click()
    
# 4. 대기시간을 적용, 랜덤으로 1초~3초사이 시간을 대기함.    
time.sleep(random.uniform(1,3)) 

# 5. 자바스크립트 소스추가 및 자바스크립트 페이지 적용 
input_js = "document.getElementById('id').value='{id}';\
    document.getElementById('pw').value='{pw}'\
    ".format(id='aaa',pw='1111')
# 자바스크립트 적용, input데이터 삽입
browser.execute_script(input_js)   

# 6. 대기시간 적용
time.sleep(random.uniform(1,3)) 
    
# 7. 로그인 버튼 클릭    
browser.find_element_by_id("log.login").click()

# 8.메인페이지에서 메일글자 클릭
elem = browser.find_element_by_link_text("메일").click()

# 9. 메일페이지에서 메일쓰기 클릭 
elem = browser.find_element_by_link_text("메일쓰기").click()

# 10. 
browser.find_element_by_id("to$0").send_keys("onulee@naver.com")

# 11.
browser.find_element_by_id("subject").send_keys("자동메일 보내기 제목")


# 12.
elem = browser.find_element_by_class_name("se2_input_syntax se2_input_text")
elem.send_keys("메일을 내용입니다.")



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



