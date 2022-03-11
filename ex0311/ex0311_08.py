# lotto 리스트에 6개의 랜덤숫자를 넣으시오.
# 중복 제거
# input 숫자 6개를 입력받으시오.
from random import *
# 1. 변수선언
lotto = []  # 로또번호
my_num = [] # 입력번호
ok_num = [] # 맞춤번호
count=0
l_count=0

# 2. 직접입력 6개 추가
for i in range(6):
    a = int(input('{}번째 숫자를 입력하세요.>>'.format(i+1)))
    my_num.append(a)
# my_num.append(int(input('숫자를 입력하세요>>')))


# 3. 랜덤숫자 6개 추가
# 무한반복
while True:
    # count 5보다 작거나 같을때 실행
    if count <= 5:
        # 랜덤숫자 가져오기
        temp = randrange(1,46)
        # 랜덤숫자가 lotto리스트에 있는지 비교
        if temp not in lotto:  # temp in lotto
            # 랜덤숫자 추가
            lotto.append(temp)
            count += 1
    else:
        print('6개의 번호가 추출되었습니다.')
        break 
    
# 4. 로또번호와 입력번호 맞는지 확인.
for i in range(6):
    if my_num[i] in lotto:
        l_count += 1 
        ok_num.append(my_num[i])   
    
# 5. 출력    
print('로또번호 : ',lotto)    
print('입력번호 : ',my_num)
print('맞춘 개수 :',l_count)
print('맞춤번호 :',ok_num)