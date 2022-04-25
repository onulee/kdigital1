import requests
from selenium import webdriver

# webdriver 크롬브라우저 변수 할당 
browser = webdriver.Chrome()
# 브라우저에서 url사이트를 실행
browser.get("http://www.naver.com")
# class name link_login 선택
elem = browser.find_element_by_class_name("link_login")
print(elem)
# elem을 클릭
elem.click()