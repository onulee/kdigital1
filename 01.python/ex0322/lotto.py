from random import *

def lottoLuck(lotto6,lottoInput,lottoLuckNo):
    for temp in lottoInput:
        if temp in lotto6:
            lottoLuckNo.append(temp)

# 로또번호 입력함수
def inputNo(lottoInput):
    for i in range(6):
        no = int(input('로또숫자를 입력하세요.>>'))
        lottoInput.append(no)

# 로또번호 생성함수
def lottoProduce(lottoNum):
    for i in range(45):
        lottoNum.append(i+1)

# 로또번호 섞기함수        
def lottosuffle(lottoNum,lotto6):
    for i in range(500):
        temp = randint(0,44)
        lottoNum[0],lottoNum[temp]=lottoNum[temp],lottoNum[0] 
    
    for i in range(6):
        lotto6.append(lottoNum[i])
               