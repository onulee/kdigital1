numbers = [273,103,5,32,65,9,72,800,99]
chk=['짝수','홀수']

for number in numbers:
    print('{:3d} : {}'.format(number,chk[number%2]))
    
    # if number%2==0:
    #     print('{} : 짝수'.format(number))
    # else:
    #     print('{} : 홀수'.format(number))    
        
    # if number>=100:
    #     print('100이상의 수 : ',number)