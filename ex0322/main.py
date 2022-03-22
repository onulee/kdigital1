import lotto
#------프로그램 시작------
lottoNum=[]
lotto6=[]
lottoInput=[]
lotto.lottoProduce(lottoNum)  #로또번호생성
lotto.lottosuffle(lottoNum,lotto6)   #로또섞기
lotto.inputNo(lottoInput)            #로또번호입력
# 맞춤번호가 몇개인지, 번호가 어떤것인지 찾는 함수

print()
print('당첨번호 :',lotto6)
print('입력번호 :',lottoInput)