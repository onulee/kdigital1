import requests
from selenium import webdriver
# selenium의 key동작 라이브러리
from selenium.webdriver.common.keys import Keys

# webdriver 크롬브라우저 변수 할당 
browser = webdriver.Chrome()
# 브라우저에서 url사이트를 실행
browser.get("http://www.naver.com")
# class name link_login 선택
elem = browser.find_element_by_class_name("link_login")
print(elem)
# elem을 클릭
elem.click()

elem = browser.find_element_by_id("id")
elem
# elem에 aaa 글자 입력
elem.send_keys("aaa")
# xpath로 선택
elem = browser.find_element_by_xpath('//*[@id="pw"]')
# elem에 1111 글자 입력
elem.send_keys("1111")
elem = browser.find_element_by_id("log.login")
# elem 클릭실행
elem.click()

# elem enter키 입력
elem.send_keys(Keys.ENTER)
# 뒤로 가기
browser.back()
# 앞으로 가기
browser.forward()
# f5 새로 고침
browser.refresh()






