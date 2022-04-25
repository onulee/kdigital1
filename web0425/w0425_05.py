import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# webdriver옵션 가져오기
options = webdriver.ChromeOptions()
# 브라우저 종료되지 않게 하는 options
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get("https://www.melon.com/chart/index.htm")
page_url = browser.page_source

# selenium으로 html소스 가져오기
soup = BeautifulSoup(page_url,"lxml")
charts = soup.find_all("tr",{"class":"lst50"})
print(charts[0].find("div",{"class":"ellipsis rank03"}).get_text())
print(charts[0].find("span",{"class":"cnt"}))

# 멜론 좋아요 숫자 출력, 숫자 js로 되어 있기에 requests로는 출력이 안됨.
# url="https://www.melon.com/chart/index.htm"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")

# charts = soup.find_all("tr",{"class":"lst50"})
# print(charts[0].find("div",{"class":"ellipsis rank03"}).get_text())
# print(charts[0].find("span",{"class":"cnt"}))


# browser = webdriver.Chrome()
# browser.get("https://www.melon.com/chart/index.htm")

# # elem = browser.find_element_by_id("query")
# browser.find_element_by_link_text("증권").click()

# # 현재 페이지 url소스 가져오기
# page_url = browser.page_source
# # res = requests.get("http://www.naver.com")
# # url소스 html파싱
# soup = BeautifulSoup(page_url,"lxml")
# # html소스 출력
# with open("elum.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())


