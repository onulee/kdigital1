# 리스트 1,45까지의 숫자를 넣어보세요.
from random import *

# lotto번호 부여 1-45
numbers = [i for i in range(1,46)]
# lotto번호 섞음.
for i in range(500):
    # 랜덤숫자 
    ran_num = randint(0,44)
    # 두수 교환
    numbers[0],numbers[ran_num] = numbers[ran_num],numbers[0]

print(numbers)


# numbers[0]=1
# numbers[1]=2
# numbers[44]=45

# numbers=[]
# for i in range(1,46):
#     numbers.append(i)
    
# print(numbers)    