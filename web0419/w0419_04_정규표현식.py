import requests
import re # 정규표현식 라이브러리
url="http://www.google.com"
res = requests.get(url) #url 파일정보 가져오기
res.raise_for_status()  # 200코드 확인

p=re.compile("ca.e")
temp = input("글자를 입력하세요.>>")
m=p.search(temp)  # match,search,findall
if m:
    print("매칭 단어 : ",m.group())  #complie 정규표현식에 맞는 부분만 출력
    print("매칭 단어 : ",m.string)  # 정규표현식이 맞으면 입력된 문자를 전체출력
    print("매칭 단어 : ",m.start()) # 맞으면 시작위치
    print("매칭 단어 : ",m.end())   # 맞으면 끝나는 위치
    print("매칭 단어 : ",m.span())  # 맞으면 시작,끝나는 위치 알려줌.
else:
    print("매칭되는 단어가 아닙니다.")

# p=re.compile("ca.e")
# # temp = input("글자를 입력하세요.>>")
# # match:정확히 일치해야지만 찾아짐. search : 단어 내에 포함되어 있으면 찾아짐.
# m=p.findall("good morning good care")
# print(m)

# if len(m)==0:
#     print("매칭되는 단어가 없습니다.")
# else:
#     print("매칭되는 단어가 있습니다.")    


# if m:
#     print("매칭 단어 : "+m.group())
# else:
#     print("매칭되는 단어가 아닙니다.")
    
# image=""
# p=re.compile("^/images")
# m=p.match("/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png")
# if m:
#     print("http://www.google.com"+m.group())
# else:
#     print("매칭되는 태그가 없습니다.")    

# 정규표현식
# p = re.compile("ca.e") #정규표현식 세팅  cafe,case,cake...caffe
# temp = input("정규표현식과 일치하는지 확인합니다. 문자를 입력하세요.>>")
# m = p.match(temp)    # 입력된 문자 case가 정규표현식과 일치하는지 확인
# if m:
#     print("일치하는 문자 : ",m.group()) 
# else:
#     print("해당문자는 일치하지 않습니다.")    


# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("비정상 입니다.")    
# print(res.text)