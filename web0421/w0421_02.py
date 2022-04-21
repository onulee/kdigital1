from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re

# 년도별 역대관객순위 5위 가져오기
for year in range(2017,2022):
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
        # 누적관객수 출력, s_cnt 마지막list를 출력
        s_cnt = screen.find_all("dd",{"class":"cont"})
        print("누적 : "+s_cnt[len(s_cnt)-1].get_text())
        # 이미지링크, url주소가 https: 없으면 추가
        s_img = screen.find("img",{"class":"thumb_img"})["src"]
        if s_img.startswith("//"):
            s_img = "https:"+s_img
        # 영화링크 출력
        s_link = screen.find("div",{"class":"info_tit"}).a["href"]
        print("링크 : "+"https://search.daum.net/search"+s_link) 
        print("-"*50)   
        
        # 영화 포스터이미지 파일저장
        s_img_res = requests.get(s_img)
        s_img_res.raise_for_status() #데이터 없을시 종료
        
        # 파일을 저장
        # 문서저장 with open("aaa.html","w",encoding="utf-8") as f:
        with open("movie{}_{}.jpg".format(year,i+1),"wb") as f:
            # requests -> res 리턴 3가지 : status_code,text,content
            f.write(s_img_res.content)
        
        # 상위 5개 이미지만 출력 , 상위 10개 출력하려면 9 입력, 30위까지 가능    
        if i>=4:
            break; 
