import requests
from bs4 import BeautifulSoup
import re
import csv

# 2020년 ~ 2022년까지 for문
for i in range(2020,2023):
    url="http://www.statiz.co.kr/salary.php?opt=0&sopt={}&te=".format(i)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")

    # csv파일 저장
    filename="{}년연봉.csv".format(i)
    f=open(filename,"w",encoding="utf-8-sig",newline="")
    writer =csv.writer(f)

    # 상단제목 저장
    title="선수 연도 팀 연봉(만원) WAR".split(" ")
    writer.writerow(title)

    # 역대 관객순위 30위 li의 상위 > ol 찾음.
    table = soup.find("table",{"class":"table table-striped"})
    # print(table)
    players = table.find_all("tr")
    for i,player in enumerate(players):
        if i==0:
            continue
        
        s_tds = player.find_all("td")
        print(s_tds[0].get_text())
        print(s_tds[1].get_text())
        print(s_tds[2].get_text())
        print(s_tds[3].get_text())
        print(s_tds[4].get_text())
        print("-"*10)
        
        # csv파일 저장
        data=[]
        data.append(s_tds[0].get_text())
        data.append(s_tds[1].get_text())
        data.append(s_tds[2].get_text())
        data.append(re.sub(r'[",]','',s_tds[3].get_text()))
        data.append(s_tds[4].get_text())
        # data 리스트 저장
        writer.writerow(data)
