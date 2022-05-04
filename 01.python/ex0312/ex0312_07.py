from random import *

# 1,100까지의 랜덤숫자 생성
# 정답이 출력될때 지금까지 입력한 숫자를 출력하시오.
temp = randint(1,100)
count=0
numSave=[]
while count<10:
    input1 = int(input('1-100사이의 원하는 번호를 입력하세요.>>'))
    numSave.append(input1) # list에 숫자 저장
    if temp==input1:
        print('정답입니다. 정답숫자 : {}'.format(input1))
        break
    elif temp>=input1:
        print('입력한 {} 숫자가 작습니다. 더 큰수를 입력하세요.!'.format(input1))
    else:
        print('입력한 {}숫자가 더 큽니다. 작은수를 입력하세요.!'.format(input1)) 
        
    count += 1 
    
if count==10:
    print('정답 숫자 : {}'.format(temp))
# 정렬후 출력을 해야 함. sort:순차정렬, reverse:역순정렬
numSave.sort(reverse=True)

print(numSave)    
                  