# 로또 맞추기 게임
from random import *
import test




randNum=[]
randNum.append(10)
# 1-45까지 랜덤숫자생성
test.lottoNum(randNum)
print(randNum)





# 로또 숫자생성 함수
# def lottoNum(randNum):
#     print(randNum)
#     randNum=10
#     return randNum
    
# def tempLotto(randNum):
#     print(randNum)   # 10 
#     randNum=500
#     return randNum
   
# #----------------------------------------
# randNum=4  #로또1-45 리스트
# randInput=[]  #입력한 로또리스트

# # 함수호출
# randNum = lottoNum(randNum)   # 10
# print(randNum)      # 4
# randNum = tempLotto(randNum)  # 10 -> 500
# print('로또숫자리스트 : ',randNum)




# for i in range(500):
#     rno = randint(0,24)
#     randNum[0],randNum[rno] = randNum[rno],randNum[0]
# print('섞은 후 리스트 : ',randNum)    

# for i in range(6):
#     input1 = int(input('로또번호를 입력하세요.>>'))
#     randInput.append(input1)