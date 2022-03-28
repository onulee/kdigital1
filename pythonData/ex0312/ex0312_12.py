list1 = []
num1 = int(input('숫자를 입력하세요.>>'))
list1.append(num1)


list2=[0,0,0,0]
nnum1 = int(input('숫자를 입력하세요.>>'))
list2[0]=nnum1
# list2[5]=10 #리스트에 없는 주소를 출력하면 에러

print("list의 크기 : ",len(list2))
print("list의 최대 주소 : ",len(list2)-1)




