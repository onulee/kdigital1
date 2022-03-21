a = 758.12345678
b = 25.05
print('%.2f' % a) 
print('{:.2f}'.format(a))

print('실수 : %010.2f' % b)
print('실수 : {:010.2f}'.format(b))

c=150.15
print('%d' % c)
print('%f' % c)
print('%s' % c)

print('-'*10)
print('*'*10)

# a = int(input('숫자를 입력하세요.>>'))
# b = int(input('숫자를 입력하세요.>>'))
# print(a+b)
# print('a={},b={},a+b={}'.format(a,b,a+b))
# -,*,/


# print('aaa')
# a=100000.123
# b=200000.45678
# print('1번째 숫자 : ',a,'2번째 숫자 :',b)
# print('1번째 숫자 :{:15.1f} 2번째 숫자 :{:,.3f}'.format(a,b))
# print('입력한 숫자는 %d 입니다.' % 100 )
# print('입력한 숫자는 %d 과 %d 입니다.' % (100,200))
# print('입력한 문자는 %s 입니다.' % '사랑')