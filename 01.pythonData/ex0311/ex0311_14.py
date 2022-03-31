# 입력한 단부터 입력단까지 출력하시오.
# 5,2 2~5단까지. 

in1 = int(input('1숫자를 입력하세요.>>'))
in2 = int(input('2숫자를 입력하세요.>>'))
if in1>in2:
    in1,in2 = in2,in1

for i in range(in1,in2+1):
    # print('[ {}단 ]'.format(i))
    for j in range(1,10):
        print('{} * {} = {} '.format(i,j,i*j),end='')
    print()    