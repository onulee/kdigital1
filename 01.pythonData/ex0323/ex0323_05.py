from urllib import request

rs = request.urlopen('https://www.naver.com')
print(rs.read())


# import time

# print('프로그램시작')
# print('cat은 무슨뜻일까요?')
# time.sleep(5)
# print('고양이 입니다.')