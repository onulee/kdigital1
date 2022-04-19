import requests
url="http://www.google.com"
res = requests.get(url) #url 파일정보 가져오기
res.raise_for_status()  # 200코드 확인

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("비정상 입니다.")    

print(res.text)