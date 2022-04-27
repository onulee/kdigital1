import requests
# url 모든 정보를 가져옴.
res = requests.get("http://www.google.com")
# res.text -> 문자출력
print(len(res.text))
print(res.text)

# 파일 저장
with open("mygoogle.html","w",encoding="utf-8") as f:
    f.write(res.text)
    