from random import *
# randNum=[i+1 for i in range(25)]

# 1.리스트 생성
randNum=[]
# 2.리스트에 1-25까지 입력
for i in range(25):
    randNum.append(i+1)
# 3.랜덤 섞기
for i in range(500):
    rno = randint(0,24)
    randNum[0],randNum[rno] = randNum[rno],randNum[0]


arrs = []
# randNum에 있는 데이터를 arrs에 list를 만들어 추가
for i in range(0,5):
    # i = 0,1,2,3,4  j=0,1,2,3,4
    arr2 = [randNum[5*i+j] for j in range(0,5)]
    # i=0           
    arrs.append(arr2)

# 2차원list 에 1-25까지의 숫자 입력
# for i in range(0,5): #0,1,2,3,4
#     # (5*0)+1,2,3,4,5  (5*1)+1,2,3,4,5  (5*2)+1,2,3,4,5
#     arr2=[5*i+j for j in range(1,6)]
#     arrs.append(arr2)

# 무한 반복
while True:
    # 2차원list에서 출력
    for arr in arrs:
        for a in arr:
            print('{:2s}'.format(str(a)),end='   ')
        print()


    # 원하는 숫자 입력    
    input1 = int(input('1-25의 숫자를 입력하세요.>>'))
    
    # 3이라는 숫자를 넣으면 3의 자리에 X 입력되도록 구현
    for i,arr in enumerate(arrs):
        if input1 in arr:
            # [1,2,3,4,5] 3의 자리 arr.index(3)->2
            arrs[i][arr.index(input1)]='X'



# 0으로 채워진 5*5 2차원 배열을 생성하시오.
# list1=[]
# for i in range(5):
#   list2 = [0 for j in range(1,6)]
#   list1.append(list2)
# print(list1)    
    
  