import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.naver.com")
elem = browser.find_element_by_id("query")
elem.send_keys("시가총액")
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_link_text("시가총액 상위종목 더보기")
elem.click()




