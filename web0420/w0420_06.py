from unittest import skip
import requests
from bs4 import BeautifulSoup
import re

url="https://www.goodchoice.kr/product/result?keyword=%EC%98%A4%EC%85%98%EB%B7%B0"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

# 정규표현식
# items = soup.find_all("li",{"class":re.compile("^list_4")})
items = soup.find_all("li",{"class":"list_4"})
name = items[0].find("div",{"class":"name"}).strong.get_text()
name = name.strip()
print(len(items))
print("숙소명 : ",name)




# name = items[2].find("img",{"class":"lazy"})["alt"]

