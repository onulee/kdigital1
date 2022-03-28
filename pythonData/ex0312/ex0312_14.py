# 4개의 값을 입력받아
# 합을 구하고 입력한 값을 출력하시오.

numbers = []
total=0
for i in range(4):
    numbers.append(int(input('{} 숫자를 입력하세요.>>'.format(i+1))))
    
for number in numbers:
    total += number
    
print('입력한 숫자 : ',numbers)
print('총합 : ',total)

    

