# 리스트,튜플, 딕셔너리, 세트
# 1. set형태 - 중복을 제거해줌.
# myset = {1,2,3,4,5,5}
# print(myset)

# 딕셔너리 추가
# dic={'name':'이름'}
# dic['id']='aaa'
# print(dic)

# 4. set 2개를 합집합,교집합,차집합,대칭집합
# adic={1,2,3,4,5}
# bdic={3,4,5,6,7}
# print(adic | bdic) # 합집합
# print(adic & bdic) # 교집합
# print(adic-bdic)   # 차집합A
# print(bdic-adic)   # 차집합B
# print(adic^bdic)   # 대칭집합

# 3. set추가, 삭제
# myset = {1,2,3}
# # 세트 추가
# myset.add(4)
# # 세트 삭제
# myset.remove(2)
# # 모두 삭제
# myset.clear()
# print(myset)


# 2.리스트를 set변경, set 다시 리스트로 변경
# mylist=[9,12,4,4,5,5,1,2,6,7,8]
# # 리스트를 set으로 타입변경
# myset = set(mylist)
# print(myset)
# # 리스트로 타입변경
# mylist = list(myset)
# print(mylist)





# saleList = ['삼각김밥','바나나','도시락','삼각김밥','도시락','오뎅','바나나']
# print(type(set(saleList)))
# saledic = set(saleList)

# print(type(saledic))

# a = {1,2,4}

# print(a)









# zipcode1 = {66012,66017,660075,66013,66019} # 10만개
# zipcode2 = {66012,66017,660075,66015,66018} # 10만개

# print(zipcode1 - zipcode2)


# numdic = {1,2,33,3,3,5,1,9,2,3}
# numdic2 = {2,3,4,5,2,3,9,10,11,13}
# print('numdic : ',numdic)
# print('numdic2 : ',numdic2)
# print('numdic | numdic2(합집합) : ',numdic | numdic2)
# print('numdic & numdic2(교집합) : ',numdic & numdic2)
# print('numdic - numdic2(차집합) :',numdic-numdic2)
# print('numdic2 - numdic(차집합) : ',numdic2-numdic)


# adic = {1:'aaa',2:'bbb',3:'ccc',1:'ddd'}
# print(adic)



# nlist1 = [1,2,5,4,8]
# nlist2 = [3,4,5,8,2]
# print(nlist1+nlist2)





# tdic={'pig':'돼지','tiger':'호랑이','lion':'사자',\
#     'dog':'개'}
# print(tdic)
# dtuple = list(tdic.items())
# dtuple.sort(reverse=True)
# tdic = dict(dtuple)
# print(tdic)
