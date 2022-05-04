str1 ='1,홍길동,100,100,200,100.0,0'
data1 = str1.split(',')
print(data1)
data1[2]=50
data1[4]=data1[2]+int(data1[3])
data1[5]=data1[4]/2
print(data1)
# if '홍길동' in str1:
#     print('홍길동이 있습니다.')
# else:
#     print('홍길동이 없습니다.')    