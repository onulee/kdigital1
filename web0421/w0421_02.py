from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re

url="https://search.daum.net/search?w=tot&q=2021%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

temp_ol = soup.find("ol",{"class":"type_plural list_exact movie_list"})
# 역대 관객순위 30위
screens = temp_ol.find_all("li")
for i,screen in enumerate(screens):
    s_cnt = screen.find_all("dd",{"class":"cont"})
    # print(len(s_cnt))
    # s_cnt 마지막list를 출력
    print(s_cnt[len(s_cnt)-1].get_text())
    
    
    # 이미지링크, url주소가 https: 없으면 추가
    s_img = screen.find("img",{"class":"thumb_img"})["src"]
    if s_img.startswith("//"):
        s_img = "https:"+s_img
    # 영화제목    
    s_title = screen.find("a",{"class":"tit_main"}).get_text()
    print(s_title)
    # 평점출력 -> float형변환
    rate = float(screen.find("em",{"class":"rate"}).get_text())
    print(rate)
    
    
    # 이미지저장
    s_img_res = requests.get(s_img)
    s_img_res.raise_for_status() #데이터 없을시 종료
    
    with open("movie2021_{}.jpg".format(i+1),"wb") as f:
        # requests -> res 리턴 3가지 : status_code,text,content
        f.write(s_img_res.content)
    
    
    # 상위 5개 이미지만 출력    
    if i>=4:
        break; 

# images = soup.find_all("img",{"class":"thumb_img"})
# for i,image in enumerate(images):
#     img_url = image["src"]
#     # startswith 함수 : 해당문자로 시작하는지 확인
#     if img_url.startswith("//"):
#         img_url = "https:"+img_url
    
#     rate = image.find("dd",{"class":"score"})
#     print(rate)
#     # 평점
#     print(rate) 
#     # 이미지 url링크   
#     # print(img_url)
    
#     # 이미지 링크를 가지고 requests함수 실행
#     img_res = requests.get(img_url)
#     img_res.raise_for_status()
    
#     # with open("aaa.html","w",encoding="utf-8") 
#     # 문자저장시 인코딩이 필요
#     with open("movie2021_{}.jpg".format(i+1),"wb") as f:
#         # requests에서 리턴하는 3가지 - status_code-상태,text-글자,content-파일
#         # f.write(res.text)
#         # f.write(img_res.content) 
#         pass   
    
    # 상위 5개 이미지만 출력    
    # if i>=4:
    #     break;       