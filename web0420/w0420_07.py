from unittest import skip
import requests
from bs4 import BeautifulSoup
import re

url="https://www.goodchoice.kr/product/result?keyword=%EC%98%A4%EC%85%98%EB%B7%B0"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

