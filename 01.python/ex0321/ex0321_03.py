# 입력된 문자의 시작이 >> 로 시작하는지 확인해서
# >> 시작하지 않으면 >>를 입력하세요.
# startswith

str1 = '4563'
if str1.startswith('>>'):
    print(str1)
else:
    print('>>'+str1)

# 입력된 문자의 첫글자가 대문자인지 확인해서 
# 대문자이면 대문자입니다. 출력하시오.

# str1 ='aaa'
# if str1[0].isupper():
#     print('첫글자가 대문자입니다.')
# else:
#     print('대문자 아닙니다.')    

# print(str1.startswith('b'))