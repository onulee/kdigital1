# 입력한 값을 + 10 를 만들어서 출력하시오.
# lambda함수 만들어 출력하시오.
# def add10(num):
#     return num+10

# 람다함수 뒤 매개변수 출력가능
# print((lambda num,num2:num+num2+10)(10,20))
# print((lambda num:num+10)(10))


list1 =[9,5,6,4,5,1,7,3,9,10]
list2=[0,1,0,0,1]
list3 =['','aaa','','a','']

for i in list2:
   if i==True:
       print(i,'True')
   else:
       print(i,'False')    

# for i in range(len(list1)):
#     list1[i] = (lambda num:num+10)(list1[i])
# print(list1)

# print(list(map(lambda num:num+10,list1)))

# 조건에 해당되는 데이터값을 리스트로 넘겨줌.
# print(list(filter(lambda num:num%2==0,list1)))







# def addNum(num1,num2):
#     sum=0
#     for i in range(num1,num2+1):
#         sum += i
#     return sum  

# print(addNum(1,100))  






# def hap(num1,num2):
#     result =num1+num2
#     return result

# # hap(1,2)

# # 함수이름 = lambda 매개변수1,매개변수2:실행문
# hap2 = lambda num1,num2:print(num1+num2)

# hap(10,20)






# 함수선언
# def fun1(v1,v2):
#     #내부함수선언- 함수내에 함수를 정의
#     def fun2(num1,num2):
#         return num1+num2
    
#     return fun2(v1,v2)

# print(fun1(10,20))
# # print(fun2(10,20))  #내부함수는 호출되지 않음.