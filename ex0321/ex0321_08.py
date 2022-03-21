# 기본값이 들어가 있는 매개변수를 사용해서
# 3개의 매개변수를 받는 함수를 선언
# v1,v2,v3 +,-,*,/    v3=1
# 4개의 값을 리턴받아서 전역부분에서 출력하시오.
# cal1(1,2)
# print('+,-,*,/의 값:')
# cal1(20,1,5)
# print('+,-,*,/의 값:')
# cal1(100,5)
# print('+,-,*,/의 값:')

def cal(v1,v2,v3=1):
    rlist=[]
    result1 = v1+v2+v3
    rlist.append(result1)
    result2 = v1-v2-v3
    rlist.append(result2)
    result3 = v1*v2*v3
    rlist.append(result3)
    result4 = v1/v2/v3
    rlist.append(result4)
    # rlist= [result1,result2,result3,result4] 
    return rlist
    # return result1,result2,result3,result4 # 튜플타입으로 리턴

temp = cal(1,2)
print('+,-,*,/의 값 :',temp[0],temp[1],temp[2],temp[3])
temp = cal(20,1,5)
print('+,-,*,/의 값 :',temp[0],temp[1],temp[2],temp[3])
temp = cal(100,5)
print('+,-,*,/의 값 :',temp[0],temp[1],temp[2],temp[3])

# def para_func(v1,v2,v3=0): # 매개변수 기본값
#     result=0
#     print(v1)
#     print(v2)
#     print(v3)
#     result=v1+v2+v3
#     return result

# hap=0
# hap = para_func(1,2,5)
# print(hap)



# 함수내 변수-지역변수, 함수를 벗어나면 사라짐.

# 함수선언 - def 함수이름
# def a(매개변수1,매개변수2):
#     return  #함수호출한 곳으로 값을 돌려줌. 없으면 생략가능

# 함수 매개변수 개수는 동일, 동일하지 않으면 error
# def cal(v1):
#     return v1
# cal(1,2)