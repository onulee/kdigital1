# 예) 245678000
# 돈을 입력받아 5만원권, 1만원, 5천원, 1천원 교환해서 출력하시오.

money = 245678000
print(format(money,','))
print('{:,}'.format(money))

a=10000
b='10,000'
c = b.replace(',','')
print(a+int(c))