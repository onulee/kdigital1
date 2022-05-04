s=[1,'홍길동']
# dictionary 선언
stu1 = {'stu_no':1,'name':'홍길동','major':'컴퓨터공학과'}

print(stu1['name'])
print(stu1.get('name'))

# print(stu1['tel']) #키값이 없으면 에러
print(stu1.get('tel'))

# 키 값 전체 출력
print(stu1.keys())
# value값 전체출력
print(stu1.values())
print(type(stu1.values()))
# 키값 리스트 출력
print(list(stu1.keys()))
# value값 리스트 출력
print(list(stu1.values()))

print(stu1.items())

print('name' in stu1)


# aa list에 11의 데이터가 있는지 확인
aa=[1,2,4,7,11,44,77]
if 11 in aa:
    print('11이 있습니다.')
    
# 딕셔너리에 name키가 있는지 확인할수 있음.    
if 'name' in stu1:  
    print('name value값 : ',stu1['name']) 
    print('name 키가 있습니다.') 
else:
    print('name 키가 없습니다.')



# s.append(100)
# print(s)

# # 딕셔너리 추가
# stu1['tel']='010-0000-0000'
# print(stu1)

# # 딕셔너리 삭제
# del(stu1['tel'])
# print(stu1)

# print(stu1['name'])







# stu = [1,'홍길동',100,100,200,100.0,0]

# aa={'no':1,'name':'홍길동','kor':100,'eng':100,'total':200,'no':200 }
# aa2={0:1,1:'홍길동',0:100}

# print(aa)
# print(stu)
# print(aa2)
# print(aa2[1])
# print(stu[1])

# aa=[
#     [1,2,3,4],
#     [5,6],
#     [7,8,9]
#     ]

# for a2 in aa:
#     for a in a2:
#         print(a)
