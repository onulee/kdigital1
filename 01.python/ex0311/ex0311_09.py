# 숫자 입력 1,10 -> 1,2,3,4,5,6,7,8,9,10
num1 = int(input('숫자를 입력하세요.'))
num2 = input('숫자를 입력하세요.')

# num1, num2 비교, num1,num2 취환
if num1 > num2:
    # temp = num1
    # num1 = num2
    # num2 = temp
    num1,num2 = num2,num1

# 전역변수
sum = 0
# eval()함수 : 문자를 숫자로 변경해주는 함수
for i in range(num1,eval(num2)+1):
    sum = sum + i
    
print('총합 : ',sum)    
