from random import *

num = randint(1,45)
count = 1
# 반복문
while True:
    input1 = int(input('{}번째 도전! 숫자를 입력하세요.>>'.format(count)))
    # 조건문 입력한 숫자와 
    if num==input1:
        print('숫자가 일치합니다.\n입력한 숫자 :{}\n 랜덤숫자 :{}'.format\
            (input1,num))
        break # while문을 빠져나옴.
    else:
        print('숫자가 일치하지 않습니다.\n 입력한 숫자:{}\n'.format\
            (input1)) 
        count += 1           
    







# input1 = int(input('숫자를 입력하세요.'))

# if input1>100:
#     print('100보다 큰수를 입력하셨습니다.')
# else:
#     print('100보다 작은 수를 입력하셨습니다.')    