# 번호,이름,국어,영어,합계,평균,등수 - 10명의 학생입력공간 생성
# stuSave = [[0]*7 for i in range(0)]
# import stu_def          #모듈선언
# import stu_def as stu   #모듈선언후 별칭사용
from stu_def import *
import json

stuSave = []  # 데이터 최종저장리스트
sCount = 0    # 학생가입인원 확인count
while True:
    choice=0  #화면출력 선택번호변수
    choice = screen_print()  # 화면출력함수 호출
    
    # isdigit() 숫자인지아닌지 확인함수
    if not choice.isdigit():  # 숫자
        print('숫자만 입력가능합니다.!!')
        continue
    # int형 변경
    choice = int(choice)
    count=0       # 학생검색 되었는지 체크하는 변수
    if choice==1: # 학생성적입력
        # 학생성적입력함수 호출 (sCount,stuSave)
        sCount = stu_input(sCount,stuSave)
    elif choice==2:
        # 학생성적 수정 (stuSave)
        stu_modify(stuSave)
        
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