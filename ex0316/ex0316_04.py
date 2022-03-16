student={
    'id':'aaa','pass':'1111','name':'홍길동','tel':'010-000-000',
    'address':'서울','gender':'male', 'hobby':'game'
}

print('[ 딕셔너리 확인 프로그램 ]')
print('1. 키값 검색')
print('2. value값 검색')
print('3. 딕셔너리 전체출력')

ch1 = int(input('원하는 번호를 입력하세요.>>'))

if ch1 == 1:
    # 1. 키값 검색
    key1=input('키를 입력하세요.>>')

    if key1 in student:
        print('키가 있습니다.')
    else:
        print('키가 없습니다.') 
elif ch1 == 2:
    # 1. value값 검색
    key1=input('value값을 입력하세요.>>')

    kchk=0
    for k in student:
        if student[k]==key1:
            print('{} : {} 값이 있습니다.'.format(k,student[k]))
            kchk=1
            break
    
    if kchk==0:
        print('{}의 value값은 없습니다.'.format(key1))      

# 2. value값 검색
# 3. 딕셔너리 전체출력 
# 원하는 번호를 입력하세요.>>
# 프로그램을 구성하시오.