student={
    'id':'aaa','pw':'1111','name':'홍길동','tel':'010-000-000',
    'address':'서울','gender':'male', 'hobby':'game'
}

# 무한 반복
while True:
    print('[ 딕셔너리 확인 프로그램 ]')
    print('1. 키값 검색')
    print('2. value값 검색')
    print('3. 딕셔너리 전체출력')
    print('4. 프로그램 종료')

    # input 의 입력데이터 str
    ch1 = input('원하는 번호를 입력하세요.>>')
    # 숫자변경이 가능한지 확인
    if not ch1.isdigit():  # 숫자
       print('숫자만 입력가능합니다.!!')
       continue
    
    # 숫자로 변경   
    ch1 = int(ch1)   

    if ch1 == 1:
        # while문 안에 넣고 0을 입력하면 메인으로 빠져나오도록 구성하시오.
        # if문을 비교
        
        while True:
            # 1. 키값 검색
            key1=input('키를 입력하세요.(0:상위메뉴 이동)>>')
            # 숫자인지 확인
            if key1.isdigit():
                if int(key1)==0:
                    print('상위메뉴로 이동합니다.')
                    break

            if key1 in student:
                print('키가 있습니다.')
            else:
                print('키가 없습니다.') 
    elif ch1 == 2:
        while True:
            kchk=0
            # 1. value값 검색
            key1=input('value값을 입력하세요.(0:상위메뉴 이동)>>')

            if key1.isdigit():
                if int(key1) == 0:
                    print('상위메뉴로 이동합니다.!!')
                    break
                
            for k in student:
                if student[k]==key1:
                    print('{} : {} 값이 있습니다.'.format(k,student[k]))
                    kchk=1
                    break
        
            if kchk==0:
                print('{}의 value값은 없습니다.'.format(key1))     
    elif ch1 == 3:
        for key in student:
            print('{} : {}'.format(key,student[key]))
            
    elif ch1 == 4:
        print('프로그램을 종료합니다.')
        break         

# 2. value값 검색
# 3. 딕셔너리 전체출력 
# 원하는 번호를 입력하세요.>>
# 프로그램을 구성하시오.