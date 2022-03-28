# para_func함수생성 가변매개변수를 사용해서
# 매개변수 합, 매개변수 모든값을 리턴해서 
# ( 함수에서 출력하면 안됨. )
# 호출한 곳에서 값을 출력하시오.
# 출력
# 매개변수 합 : 1111
# 매개변수 값 : 10,20,30,40.....100
# para_func(10,20,30,40,50,60,70,80,90,100)

# 함수선언
def para_func(num,*para):
    total=0
    temp=[]
    # 가변매개변수를 합, 리스트에 추가
    for i in num:
        total = total + i
        temp.append(i)
    
    return total,temp

num=[]
while True:
    temp_num = int(input('숫자를 입력하세요.>>'))
    if temp_num==0:
        print('매개변수 입력종료')
        break
    num.append(temp_num)

data1 = para_func(num)
# 튜플타입 (total,temp)
print(type(data1))
print(data1)
print('매개변수 합 :',data1[0])
print('매개변수 값 :',data1[1])


# 옵션2. 가변매개변수로 받지 않아도 됨.
# 매개변수값을 입력받아, 받고 싶은 만큼 받아서 출력







# 디폴트 매개변수값, 가변매개변수를 사용하면 개수가 맞지 않아도 실행됨.
# def para_func(v1,v2,v3=0,*para):
#     print('v1 : ',v1)
#     print('v2 : ',v2)
#     print('v3 : ',v3)
#     for i in para:
#         print('para : ',i)
#     return

# para_func(1,2,3,4)
# print('프로그램 실행완료')


# def 함수이름() 함수선언
# (매개변수1,매개변수2) - 매개변수는 호출개수와 함수선언의 매개변수 개수 같아야 함.
# 매개변수 기본값설정, 매개변수에 디폴트값을 설정할수 있음. 예)v3=10
# 기본값 설정이 되어 있는 매개변수는 호출에서 값이 입력되지 않으면
# 기본값이 세팅이 됨.
# return 개수는 상관없음. 리턴변수는 2개이상일때 튜플타입, 없으면 생략가능
