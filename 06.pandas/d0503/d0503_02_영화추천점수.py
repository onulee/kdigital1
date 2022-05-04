import requests
from bs4 import BeautifulSoup
import re
import csv

# csv파일 저장
filename="역대관객순위.csv"
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer =csv.writer(f)

# 상단제목 저장
title="영화제목 평점 개봉일 누적인원".split(" ")
writer.writerow(title)

# 년도별 역대관객순위 5위 가져오기
for year in range(2016,2022):
    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")

    # 역대 관객순위 30위 li의 상위 > ol 찾음.
    temp_ol = soup.find("ol",{"class":"type_plural list_exact movie_list"})
    # 역대 관객순위 li 30개 찾음.
    screens = temp_ol.find_all("li")
    for i,screen in enumerate(screens):
        # 영화제목    
        s_title = screen.find("a",{"class":"tit_main"}).get_text()
        print("영화제목 : "+s_title)
        # 평점출력 -> float형변환
        rate = float(screen.find("em",{"class":"rate"}).get_text())
        print("평점 : ",rate)
        # 개봉일 출력, s_date 마지막list를 출력
        s_date = screen.find_all("dd",{"class":"cont"})
        print("개봉일 : "+s_date[len(s_date)-3].get_text())
        ss_date = s_date[len(s_date)-3].get_text().strip()
        # 누적관객수 출력, s_cnt 마지막list를 출력
        s_cnt = screen.find_all("dd",{"class":"cont"})
        ss_cnt = s_cnt[len(s_cnt)-1].get_text()  
        # 누적인원 100,000,000명
        ss_cnt = re.sub(r'[명,]','',ss_cnt)
        # ss_cnt = re.sub(r'[^0-9]','',ss_cnt)
        print("누적인원 : "+ss_cnt)
        
        
        
        # csv파일 저장
        data=[]
        data.append(s_title)
        data.append(rate)
        data.append(ss_date)
        data.append(ss_cnt)
        # data 리스트 저장
        writer.writerow(data)
        
        # 상위 5개 이미지만 출력 , 상위 10개 출력하려면 9 입력, 30위까지 가능    
        if i>=4:
            break; 
        
f.close()        
# ------------------------------
# 2. csv파일 불러오기
import pandas as pd
df = pd.read_csv('역대관객순위.csv')  

# 3. 추천점수 컬럼 생성
df['추천점수'] = 0
df['추천점수'] = df['평점']*df['누적인원']/100 


# 4. 추천점수가 높은 순으로 출력
print(df.sort_values('추천점수',ascending=False))


        