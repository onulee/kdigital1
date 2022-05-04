# 입력은 url을 입력받음.

# 힌트 : http://www. replace
# naver.com
# .com . index 슬라이싱[0:.까지의 index번호 ] 
# naver + 글자총길이수 + c가 들어간 개수 + '!!'
# 비밀번호생성 : naver201!!

url = 'http://www.naver.com'
temp = url.replace('http://www.','')
# naver.com
print(temp.index('.'))
# temp[0:5]
temp = temp[0:temp.index('.')]
print(temp+str(len(url))+str(url.count('c'))+'!!')

