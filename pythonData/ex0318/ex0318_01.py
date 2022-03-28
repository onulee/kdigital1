from random import *
mark_lotto=[i+1 for i in range(45)]   #표시하는 번호 리스트
in_num = []    # 입력하는 번호 리스트
lotto=[]    # 당첨번호 리스트
in_lotto=[] # 당첨된 번호 리스트
lotto_num=[i+1 for i in range(45)] #로또번호 리스트
reward = ['꽝!','1천원','5백만원','5천만원','1억원','50억원','100억원']
# lotto = sample(lotto_num,6)

### 1. 로또당첨 번호 생성
for i in range(500):
    rno = randint(0,44)
    lotto_num[0],lotto_num[rno] = lotto_num[rno],lotto_num[0]
lotto = lotto_num[:6]  
print('당첨번호 :',lotto)  

### 2. 로또번호 입력
for i in range(6):
    count=0 #45까지 출력되도록 체크하는 변수
    print('[ LOTTO CARD ]')
    for i in range(5):
        for j in range(10):
            if count < 45:
                print('{:2s}'.format(str(mark_lotto[10*i+j])),end=' ')
                count += 1
            else:
                break    
        print() 
    
    tempNum = int(input('로또번호를 입력하세요.>>'))
    in_num.append(tempNum)  #입력한 숫자 입력리스트에 추가
    mark_lotto[tempNum-1]='X'
    

### 3. 당첨확인
for num in in_num: #(index번호,데이터값)
    if num in lotto:
        in_lotto.append(num)

print('당첨번호 :',lotto)          
print('입력번호 :',in_num)    
print('당첨 개수 :{}개, {} '.format(len(in_lotto),in_lotto)) 
print('당첨 금액 :',reward[len(in_lotto)])




# 자신이 입력한 6개의 숫자와 로또 당첨번호 6개와 비교해서
# 몇개를 맞췄는지 출력하는 프로그램을 구현하시오.
# [ 옵션 ]
# 자신이 입력한 번호가 보여지면서 입력을 받음.
# 1-45까지의 번호가 있고, 입력한 번호는 X가 표시가 
# 되게 화면구현
# 1,2,X,4,5,6,X,8,9,10
# 11,12,13,14,15,16,17,18,19,20
# 번호를 입력하세요.>>
# 당첨번호 : 32,1,42,17,39,19
# 입력번호 : 1,2,3,4,5,32
# 당첨개수 : 1,32
# 당첨금액 : 5백만원
# 6개 : 100억
# 5개 : 50억
# 4개 : 1억
# 3개 : 5천만원
# 2개 : 5백만원
# 1개 : 1천원
# 0개 : 꽝!







# 0-44까지 리스트
# lotto = [i+1 for i in range(45)]
# print(lotto)

# shuffle(lotto)
# print(lotto)
# print(sample(lotto,6))


# for i in range(500):
#     rno = randint(0,44)
#     lotto[0],lotto[rno] = lotto[rno],lotto[0]

# print(lotto)    



# 6개를 수를 뽑아보세요.
# lottoNum=[]
# count=0
# while True:
#     if count<6:
#         rno = randint(0,44)
#         if not lotto[rno] in lottoNum:
#             lottoNum.append(lotto[rno])
#             count += 1    
    
#     break     
    
# print(lottoNum)    
    




# lotto = range(1,46)
# print(list(lotto))

# lotto=[]
# for i in range(45):
#     lotto.append(i+1)
# print(lotto)    

# lotto = [i+1 for i in range(45)]
# print(lotto)





# random() 0*10<=random()<1*10
# 0+1<= x <10+1  int(1)<= int(x) <int(11)  1<=x<=10
# random()함수로 1~45 숫자 1개를 출력
# print(int(random()*45)+1)
# # randint() 1~45 숫자1개를 출력
# randint(1,45)

