aa= [ 1,'홍길동',100,100,200,100.0,0]
print(type(aa))
for i in range(len(aa)):
    print('{} : {}'.format(i,aa[i]))


stu1 = {'no':1,'name':'홍길동','kor':100,'eng':100,'total':200,\
        'avg':100.0,'rank':0}
print(type(stu1))
# 딕셔너리 전체출력 for문
for key in stu1:
    print('{} : {}'.format(key,stu1[key]))


# while True:
#     search = input('키값을 입력하세요.>>')
#     # 딕셔너리에서 키값 확인
#     if search in stu1:
#         print(stu1[search])
#     else:
#         print('키값이 없습니다. 다시 입력하세요.!!')
#         print()    