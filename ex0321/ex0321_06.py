a=20
b=10

def cal1(a,b):
    result=0
    result=a+b
    a=100
    b=200
    return result

def cal2(a,b):
    result=0
    result=a+b
    a=1
    b=2
    return result
    

cal1(a,b) 
cal2(a,b)               # 1.a=100,b=200  2.a=1,b=2   3.a=20,b=10
print('a,b의 값 :',a,b)  # a,b의 값은 얼마일까요?  

    
    





# list1 = [1,2,3]
# list2 = list1
# list2[0]=100
# print(list1[0]) #

# 변수
# a = 5
# b = a
# b = 10
# print(a)  # 5