from random import *
# randNum=[i+1 for i in range(25)]

randNum=[]
for i in range(25):
    randNum.append(i+1)
# randNum=[1,2,3,4,.....24,25]
#          0,1,2,3,.....23.24

print('섞기 전 리스트 : ',randNum)

for i in range(500):
    rno = randint(0,24)
    randNum[0],randNum[rno] = randNum[rno],randNum[0]
    
print('섞은 후 리스트 : ',randNum)    


# aa=[1,2,3,4,5]
# while True:
#     input1 = int(input('1-5사이의 숫자를 입력하세요.>>'))
#     for i,a in enumerate(aa):
#         if a == input1:
#             aa[i] = 'X' 
        
#     print(aa)       