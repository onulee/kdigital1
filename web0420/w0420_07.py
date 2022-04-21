import requests
from bs4 import BeautifulSoup
import re

url="http://browse.auction.co.kr/search?keyword=tv&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=tv&acode=SRP_SU_0100&arraycategory=&encKeyword=tv"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

div1 = soup.find("div",{"id":"section--inner_content_body_container"})
items = div1.find_all("div",{"class":"itemcard"})
for i,item in enumerate(items):
    title = item.find("span",{"class":"text--title"}).get_text()
    temp_rate = item.find("div",{"class":"seller_awards"})
    if temp_rate:
        rate = temp_rate["title"]
        rate = float(re.sub(r'[^0-9.]','',rate))  
        # sub() 정규표현식을 가지고 해당되는 문자를 대체해서 변경함.
        # re.sub('r[정규표현식]','대체할문자',해당변수)
        if rate>4.5:
            pass
            
    else:
        pass
         
    print(rate)
    print("{}.{}".format(i+1,title))
    print("-"*50)
    

