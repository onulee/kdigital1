# 두수를 입력받아 홀수의 값의 합을 출력하시오.
# 5,27 -> 홀수의 합을 구하면 됨.
n1 = int(input('1숫자를 입력하세요.>>'))
n2 = int(input('2숫자를 입력하세요.>>'))

sum=0
for i in range(n1,n2+1):
    if i%2 == 1:
        sum = sum + i

print('총합 : ',sum)        


# 0-100 7의 배수의 합을 구하시오.
# 합을 구하는 변수
# sum=0
# for i in range(0,100):
#     if i%7==0:
#         sum = sum + i
        
# print('7의 배수의 합 : ',sum)        


# # 0-100 홀수의 합을 구하시오.
# sum1 = 0
# for i in range(0,100):
#     if i%2 == 1:
#         sum1 = sum1 + i

# print('홀수의 합 :',sum1)