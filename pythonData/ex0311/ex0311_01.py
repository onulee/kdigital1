input1 = int(input('점수를 입력하세요.>>'))

if input1>=90:
    print('A',end='')
    if input1>=98:
        print('+')
    elif 93>=input1>=90:
        print('-')    
elif input1>=80:
    print('B')    
elif input1>=70:
    print('C')
elif input1>=60:
    print('D') 
else:
    print('F')       




# 60점이상이면 합격, 60점미만 불합격출력
# if input1>=60:
#     print('합격')
# else:
#     print('불합격')



# 5보다 크고 10보다 작은수 비교
# if 5<input1<10:
#     print('5보다크고 10보다 작은 수입니다.')
    
# if 5<input1 and input1<10:
#     print('5보다 크고, 10보다 작은 수입니다.')    


# 3의 배수인지 아닌지 확인
# if input1%3 == 0:
#     print('3의 배수입니다.')
# else:
#     print('3의 배수가 아닙니다.')    



# 짝수입니다. 홀수입니다.
# if input1%2==0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')    



# 입력받음 - str()-> int()
# input1 = int(input('숫자를 입력하세요.>>'))

# if input1>10:
#     print('10보다 큽니다.')
# else:
#     print('10보다 작습니다.')    


