# 번호,이름,국어,영어,합계,평균,등수 - 10명의 학생입력공간 생성

# stuSave = [[0]*7 for i in range(0)]
# 데이터 최종저장리스트
stuSave = []
# 학생가입인원 확인count
sCount = 0
while True:
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생성적입력') # 완료
    print('2. 학생성적수정') # 완료
    print('3. 학생성적삭제') # 완료
    print('4. 학생성적전체출력') # 완료
    print('5. 학생검색출력')     # 완료
    print('6. 등수처리')         
    print('0. 프로그램종료')     # 완료
    print('-'*25)
    # 숫자만 받는데, 문자를 입력하면 에러
    # 숫자만 받도록 변경
    choice = input('원하는 번호를 입력하세요.>>')
    
    # isdigit() 숫자인지아닌지 확인함수
    if not choice.isdigit():  # 숫자
        print('숫자만 입력가능합니다.!!')
        continue
    # int형 변경
    choice = int(choice)
    count=0  # 학생검색 되었는지 체크하는 변수
    if choice==1:
        print('-- {}번째 학생등록 -- '.format(sCount+1))
        sName = input('학생이름을 입력하세요.>>')
        kor = int(input('국어 점수를 입력하세요.>>'))
        eng = int(input('영어 점수를 입력하세요.>>')) 
        # 리스트 추가
        temp ={'stuno':sCount+1,'stuname':sName,'kor':kor,'eng':eng,\
            'total':kor+eng,'avg':(kor+eng)/2,'rank':0}
        stuSave.append(temp)
        sCount += 1 #학생인원 count 1증가
        print('학생성적이 저장되었습니다.')
    elif choice==2:
        print('[ 학생성적 수정페이지 ]')
        print('-'*50)
        searchName = input('수정할 이름을 입력하세요.>>')
        for i,stu in enumerate(stuSave):
            if searchName in stu.values():
                print('{} 학생이 검색되었습니다.'.format(searchName))
                print('[ 점수 수정 ]')
                print('1.국어점수 수정')
                print('2.영어점수 수정')
                print('0.상위메뉴 이동')
                searchNo = int(input('수정할 과목 번호를 입력하세요.>>'))
                
                if searchNo==1:   # 국어점수수정
                    print('현재 국어점수 :',stu['kor'])
                    score = int(input('변경할 국어점수 입력>>'))
                    stu['kor']=score    #현재국어점수 = 변경국어점수
                    # 합계,평균 점수 변경
                    stu['total'] = stu['kor']+stu['eng']
                    stu['avg'] = stu['total']/2
                    print('국어점수가 변경되었습니다.!!')
                elif searchNo==2: # 영어점수수정
                    print('현재 영어점수 :',stu['eng'])
                    score = int(input('변경할 영어점수 입력>>'))
                    stu['eng']=score    #현재국어점수 = 변경국어점수
                    # 합계,평균 점수 변경
                    stu['total'] = stu['kor']+stu['eng']
                    stu['avg'] = stu['total']/2
                    print('영어점수가 변경되었습니다.!!')
                
                elif searchNo==0: # 상위메뉴이동
                    print('상위메뉴로 이동합니다.')
                count=1 # 학생검색이 됨.
                break
        if count==0:    
            print('{} 학생이 없습니다.'.format(searchName))
    elif choice==3:
        print('학생성적 삭제를 선택하셨습니다.')
        searchName = input('삭제할 이름을 입력하세요.>>')
        count=0
        for i,stu in enumerate(stuSave):
            if searchName in stu.values():
                del(stuSave[i])
                print('{} 학생이 삭제되었습니다.'.format(searchName))
                count=1
                break
        if count==0:
            print('{} 학생이 없습니다.'.format(searchName)) 
        
    elif choice==4:
        print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
        print('-'*60)
        # [[1,홍길동,100,100,200,100.0,0]]
        for stu in stuSave:
            # print정렬
            print(stu['stuno'],stu['stuname'],stu['kor'],stu['eng'],\
                stu['total'],stu['avg'],stu['rank'],sep='\t')
            # for k,v in stu.items():
            #    print('{}\t'.format(v),end='') 
            # print() #줄바꿈
    elif choice==5:
        searchName = input('출력할 학생이름을 입력하세요.>>')
        count=0
        for i,stu in enumerate(stuSave):
            if searchName in stu.values():
                print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
                print('-'*60)
                print(stu['stuno'],stu['stuname'],stu['kor'],stu['eng'],\
                stu['total'],stu['avg'],stu['rank'],sep='\t')
                count=1
                break
        if count==0:
            print('{} 학생이 없습니다.'.format(searchName)) 
    
    elif choice==6:
        for stu in stuSave:
            rcount=1
            for stu2 in stuSave:
                if stu['total'] < stu2['total']: #total점수 비교
                    rcount += 1    # stu2가 더 클경우 1증가
            stu['rank'] = rcount   # 등수입력        
        
        print('등수처리가 완료되었습니다.')        
                
    elif choice==0:
        print('프로그램을 종료합니다.')
        break