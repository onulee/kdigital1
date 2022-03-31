from lotto import *

# import lotto
#------프로그램 시작------
lottoNum=[]
lotto6=[]
lottoInput=[]
lottoLuckNo=[]
lottoProduce(lottoNum)  #로또번호생성
lottosuffle(lottoNum,lotto6)   #로또섞기
inputNo(lottoInput)            #로또번호입력
lottoLuck(lotto6,lottoInput,lottoLuckNo)   #로또번호확인
# 맞춤번호가 몇개인지, 번호가 어떤것인지 찾는 함수

print('당첨번호 :',lotto6)
print('입력번호 :',lottoInput)
print('당첨개수 : {}, 당첨해당번호 : {}'.format(len(lottoLuckNo),lottoLuckNo))