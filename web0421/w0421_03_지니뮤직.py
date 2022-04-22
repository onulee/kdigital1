import requests
from bs4 import BeautifulSoup
import re

for page in range(4):
# page 1,2,3,4 까지 반복진행
    url="https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220421&hh=15&rtm=Y&pg={}".format(page+1)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")


    temp_tbody = soup.find("table",{"class":"list-wrap"}).tbody
    musics = temp_tbody.find_all("tr",{"class":"list"})

    for i,music in enumerate(musics):
        # 곡명 출력 - 공백제거 strip()
        title = music.find("a",{"class":"title ellipsis"}).get_text().strip()
        print("곡명 : "+title)
        # 아티스트 출력
        artist = music.find("a",{"class":"artist ellipsis"}).get_text().strip()
        print("아티스트 : "+artist)
        # 이미지 링크출력
        img_url = music.find("a",{"class":"cover"}).img["src"]
        if img_url.startswith("//"):
            img_url = "https:"+img_url
        print("이미지 링크 : "+img_url)
        print("-"*50)

        img_url_res = requests.get(img_url)
        img_url_res.raise_for_status() #에러시 종료
        with open("img_{}_{}.jpg".format(page+1,(i+1)),"wb") as f:
            f.write(img_url_res.content)


