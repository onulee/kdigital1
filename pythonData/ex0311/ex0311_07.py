import random
from random import *

# lotto 6개를 저장해서 출력하시오.
# list에 중복을 저장한 후 저장하시오.
# 로또번호 저장리스트
lotto = []
# 6번 반복
for i in range(0,6):
    # 랜덤숫자 발생
    temp = randrange(1,46)
    if temp not in lotto:  # temp in lotto
        # 랜덤숫자 추가
        lotto.append(temp)
print(lotto)

count=0
# 무한반복
# while True:
#     # count 5보다 작거나 같을때 실행
#     if count <= 5:
#         # 랜덤숫자 가져오기
#         temp = randrange(1,46)
#         # 랜덤숫자가 lotto리스트에 있는지 비교
#         if temp not in lotto:  # temp in lotto
#             # 랜덤숫자 추가
#             lotto.append(temp)
#             count += 1
#     else:
#         print('6개의 번호가 추출되었습니다.')
#         break 
# print(lotto)               