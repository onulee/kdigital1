stulist=[
    {'stuno':1,'stuname':'홍길동','kor':100,'eng':100,\
            'total':100+100,'avg':(100+100)/2,'rank':0},
    {'stuno':2,'stuname':'이순신','kor':99,'eng':100,\
            'total':99+100,'avg':(99+100)/2,'rank':0},
    {'stuno':3,'stuname':'유관순','kor':99,'eng':99,\
            'total':99+99,'avg':(99+99)/2,'rank':0}
]

while True:
    print(stulist)
    searchName = input('이름을 검색하세요.>>')
    count=0
    for i,stu in enumerate(stulist):
        if searchName in stu.values():
            print('{}이 있습니다.'.format(searchName))
            del(stulist[i])
            print('{}이 삭제되었습니다.'.format(searchName))
            count=1
            break
    if count==0:
        print('{}이 없습니다.'.format(searchName))    
    

# searchName = input('찾고하는 이름을 입력하세요.>>')
# for stu in stulist:
     



# studic = {'stuno':1,'stuname':'홍길동','kor':100,'eng':100,\
#             'total':100+100,'avg':(100+100)/2,'rank':0}

# print(studic.items())

# # 키값만 가져옴.
# for k in studic.keys():
#     print(k,studic[k]) # value값 출력

# # value값만 가져옴
# for v in studic.values():
#     print(v)

# for k,v in studic.items():
#     print('{}:{}'.format(k,v),end=' ')



# # 변수선언, 수정
# a=1
# print(a)
# a=3
# print(a)

# # 리스트 출력,추가,삭제,변경
# list1 = [1,{1:'aaa'},[1,2,3],3,4,5]
# list1[3]=5
# list1.append(7)
# print(list1)
# del(list1[3])
# print(list1)

# # 튜플=리스트와 읽어오는 방법은 동일, 변경,삭제,추가 안됨.
# dtuple = (1,{1:'aaa'},[1,2,3],3,4,5)
# print(dtuple[0])

# # 딕셔너리 - 출력,변경,추가,삭제
# datadic={1:'aaa',2:'bbb','id':'aaa'}
# print(datadic[1])
# datadic[1]='ddd'
# print(datadic)
# datadic['pw']='1111'
# print(datadic)
# del(datadic[2])
# print(datadic)



