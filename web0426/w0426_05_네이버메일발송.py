import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import re
import csv
import smtplib
from email.mime.text import MIMEText

# 구글에서 한소희 검색
# 한소희, 현금으로 19억 집 샀다…현빈 신혼집 마을로 이사 검색내용 보내기

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
url="https://namu.wiki/w/%EC%84%B8%EC%A2%85"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
# print(soup)

### 메일 발송 ###

# 글쓰기 제목,내용
title="파이썬 이메일 보내기 수업2"
content ="드라마 '부부의 세계'로 알려진 배우 한소희(27)가 대출 없이 19억원대의 고급빌라를 구매했다.\
지난 26일 스카이데일리에 따르면 한소희가 최근 경기 구리 아천동에 위치한 '빌라드그리움W'의 한 호실을 매입했다. 거래액은 19억5000만원으로 대출 없이 전액 현금으로 샀다.\
등기부등본상 전용면적 155.67㎡(약 47.09평) 규모로 부동산 관계자들에 따르면 한소희가 소유하고 있는 호실의 공급면적은 83평형(약 274㎡)이다.\
익명을 요구한 한 공인중개사는 해당 매체에 '지난해 여름 분양가가 21억1000만원 정도였는데 그것보단 싸게 샀다'며 '한소희가 직접 발품을 팔아 매입한 것으로 알고 있다'고 말했다."

# MIME 객체
msg = MIMEText(content)
msg['From']="onulee@naver.com"
msg['To']="onulee@naver.com"
msg['Subject']=title

# 메일서버주소 정보 smtp.naver.com/587
s = smtplib.SMTP("smtp.naver.com",587)
# 메일 서버 접근
s.starttls()
# 메일 서버 로그인(id,pw입력)
s.login("onulee@naver.com","1111")
# 메일 발송(보내는주소, 받는주소, 내용)
s.sendmail("onulee@naver.com","onulee@naver.com",msg.as_string())
# 메일 닫기
s.close()

