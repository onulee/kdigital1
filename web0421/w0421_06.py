import requests
from bs4 import BeautifulSoup
import csv  #csv파일 라이브러리
import re

url="https://www.melon.com/chart/index.htm"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
rank = soup.find("div",{"class":"service_list_song type02 d_song_list"})
print(rank)