# 두수를 입력받아 사칙연산이 되도록 프로그램 하시오.
# 무한 반복할수 있도록 합니다.
# 출력
# 2 + 1 = 3
# 2 - 1 = 1
# 2 * 1 = 2
# 2 / 1 = 2
# 첫번째 수를 입력하세요.>>
# 두번째 수를 입력하세요.>>
# 2번까지 실행하고 2번이후에는 입력한 값을 출력하시오.



# list 깊은 복사 ( 새로운 공간을 만들어서 생성 )
list1 = [ [0]*2 for _ in range(5) ]
# [[0]*2]*5  # 얕은 복사(동일한 공간을 사용-주소값 동일)
tno=0
while True:
    print(list1)
    if tno<len(list1):   #len list의 길이를 알려줌.
        no1 = int(input('첫번째 수를 입력하세요.>>'))
        no2 = int(input('두번째 수를 입력하세요.>>'))
        list1[tno][0] = no1
        print(list1[tno][0])
        list1[tno][1] = no2
        print(list1[tno][1])

        print('{} + {} = {}'.format(no1,no2,no1+no2))
        print('{} - {} = {}'.format(no1,no2,no1-no2))
        print('{} * {} = {}'.format(no1,no2,no1*no2))
        print('{} / {} = {}'.format(no1,no2,no1/no2))
        tno += 1
    else:
        break  
 
print(list1)    
      