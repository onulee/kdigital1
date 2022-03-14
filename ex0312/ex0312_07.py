from random import *

# 1,100까지의 랜덤숫자 생성
temp = randint(1,100)

while True:
    input1 = int(input('1-100사이의 원하는 번호를 입력하세요.>>'))
    
    if temp==input1:
        print('정답입니다. 정답숫자 : {}'.format(input1))
        break
    elif temp>=input1:
        print('입력한 {} 숫자가 작습니다. 더 큰수를 입력하세요.!'.format(input1))
    else:
        print('입력한 {}숫자가 더 큽니다. 작은수를 입력하세요.!'.format(input1))        