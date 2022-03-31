foods=['떡볶이','짜장면','라면','피자','맥주']
sides = ['오뎅','단무지','김치','피클','땅콩']

# 1개의 주소값으로 2개가 동시에 사용되어짐

# 복사할땐 copy명령어를 사용

# foods2 = foods.copy()
foods2 = foods[:]
foods2[0]='안팔어'
print(foods)




# 튜플형태의 list타입으로 변경
# 2개의 list를 dic타입으로 변경
# tuplist = list(zip(foods,sides))
# print(type(tuplist))
# print(type(dict(tuplist)))
# print(dict(tuplist))




# for food,side in zip(foods,sides):
#     print('{}:{}'.format(food,side))

# min최소값을 리턴, max최대값 리턴
# idx = min(5,3)

# if len(foods)<len(sides):
#     idx = len(foods)
# else:
#     idx = len(sides)    

# idx=0
# idx = min(len(foods),len(sides))
# for i in range(idx):
#     print(foods[i],":",sides[i])


# for문의 종류

# complist = [0,1,2,3,4,5,6,7,8,9]
# complist2 = [3,6,9,12,18]

# 한줄for문
# alist=[ i for i in range(1,21) if i%3==0 ]
# print(alist)

# alist=[]
# 기본for문
# for i in range(1,21):
#     if i%3==0:
#         alist.append(i)
# print(alist)        
    



# 기본for문
# alist=[]
# for i in range(0,10):
#     alist.append(i)
# print(alist)    

# 한줄 for문
# alist = [ i for i in range(0,10) ]
# print(alist)




