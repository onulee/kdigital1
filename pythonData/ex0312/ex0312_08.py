total,i=0,0

for i in range(1,100):
    if i%3==0:
        continue
    total += i
    print('{},{}'.format(i,total))
    if total>100:
        break

print('합 :{}'.format(total))
print('100을 넘었을때 숫자 :',i)     


# a = input('문자를 입력하세요.')
# if a=='$':
#     print('$문자입니다.')
# else:
#     print('$문자가 아닙니다.')    