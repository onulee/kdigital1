from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re

url="https://search.daum.net/search?w=tot&q=2021%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

images = soup.find_all("img",{"class":"thumb_img"})
for i,image in enumerate(images):
    img_url = image["src"]
    # startswith 함수 : 해당문자로 시작하는지 확인
    if img_url.startswith("//"):
        img_url = "https:"+img_url
        
    print(img_url)
    
    # 이미지 링크를 가지고 requests함수 실행
    img_res = requests.get(img_url)
    img_res.raise_for_status()
    
    # with open("aaa.html","w",encoding="utf-8") 
    # 문자저장시 인코딩이 필요
    with open("movie2021_{}.jpg".format(i+1),"wb") as f:
        # requests에서 리턴하는 3가지 - status_code-상태,text-글자,content-파일
        # f.write(res.text)
        f.write(img_res.content)    
    
    # 상위 5개 이미지만 출력    
    if i>=4:
        break;       