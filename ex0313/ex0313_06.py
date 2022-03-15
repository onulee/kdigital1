aa=[1,2,333,6,555,6,77,8,9]
print("1 : ",aa)

# 깊은 복사 aa가 바뀌어도 bb는 바뀌지 않음.
# bb = aa.copy()
# aa[0] = 500
# print('aa list[aa[0]=500] : ',aa)
# print('bb list : ',bb)

# 얕은 복사는 주소값을 복사해서 aa가 바뀌면 bb도 바뀜
# bb = aa
# aa[0] = 500
# print('aa list[aa[0]=500] : ',aa)
# print('bb list : ',bb)




# bb = aa.sort()
# print("2 : ",bb)

# cc = sorted(aa)
# print('3 : ',cc)

# aa[0]=500

# print("4 : ",aa)
# print("5 : ",cc)



# 추가 list로 추가
# aa.extend([1,2,3])
# print(aa)


# 찾고자 하는 데이터가 몇개있는지 확인
# print(aa.count(6))

# 찾는 데이터 위치를 알려줌.
# idx = aa.index(77)
# print(idx)

# if 77 in aa:
#     print('77 값이 있습니다.')


# 특정위치에 값을 추가
# aa.insert(2,3)
# print(aa)
# 마지막에 값 추가
# aa.append(44)
# print(aa)

# 역순정렬
# aa.sort(reverse=True)
# print(aa)

#순차정렬
# aa.sort()
# print(aa)


# aa.pop()
# 일부 삭제 
# aa.pop(2)
# print(aa)

# list의 데이터를 검색해서 리스트 삭제함.
# 데이터 값으로 삭제
# for i in range(len(aa)):
#     if 6 in aa:
#         aa.remove(6)
# print(aa)

# aa.clear()
# aa=[]
# print(aa)
# print(type(aa))


# # 삭제
# aa[1:4]=[]
# print(aa)


# 삭제방법1 del(aa) 변수자체도 제거
# del(aa)
# print(aa) # del(aa)후 출력을 하려면 에러
# print(type(aa)) 


# 삭제방법2 aa=None 변수만 존재함.
# print(aa)
# print(type(aa)) # 타입이 NoneType

# 삭제방법3 aa=[] 타입의 형태는 남아 있음.
# aa=[]
# aa.clear() # 전체삭제 타입은 남아 있음.
# print(aa)
# print(type(aa)) #타입이 list

