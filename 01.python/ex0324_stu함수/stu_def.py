import os
import json
import student

stuSave=[]  #전역변수
sCount=[0]
count=0       # 학생검색 되었는지 체크하는 변수
# 1. json읽기 함수
def jsonRead():
    global stuSave
    if 'stuData.json' in os.listdir():
        stuSave = json.load(open('stuData.json','r'))
    else:
        stuSave=[]    

# json저장 함수
def jsonSave():
    if 'stuData.json' in os.listdir():
        json.dump(stuSave,open('stuData.json','w'))
    else:
        json.dump(stuSave,open('stuData.json','w'))
            

# 학생번호 증가함수    
def stuCount():
    global sCount
    
    if len(stuSave)==0:
        sCount=1
    else:
        sCount = stuSave[-1]['stuno']+1
    return sCount   


# 화면출력함수
def screen_print():
    jsonRead()
    stuCount()
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
        # choice=0
    return int(choice)

# 성적입력함수
def stu_input():
    global sCount
    print('-- {}번째 학생등록 -- '.format(sCount))
    sName = input('학생이름을 입력하세요.>>')
    kor = int(input('국어 점수를 입력하세요.>>'))
    eng = int(input('영어 점수를 입력하세요.>>')) 
    # 리스트 추가
    temp ={'stuno':sCount,'stuname':sName,'kor':kor,'eng':eng,\
        'total':kor+eng,'avg':(kor+eng)/2,'rank':0}
    # Student객체 저장
    # temp = student.Student(sCount,sName,kor,eng)
    stuSave.append(temp)
    print(stuSave)
    jsonSave()  # json저장함수 호출
    sCount += 1 #학생인원 count 1증가
    print('학생성적이 저장되었습니다.')

# 학생성적 수정함수
def stu_modify():
    count=0
    jsonRead()
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
                jsonSave()
                print('국어점수가 변경되었습니다.!!')
            elif searchNo==2: # 영어점수수정
                print('현재 영어점수 :',stu['eng'])
                score = int(input('변경할 영어점수 입력>>'))
                stu['eng']=score    #현재국어점수 = 변경국어점수
                # 합계,평균 점수 변경
                stu['total'] = stu['kor']+stu['eng']
                stu['avg'] = stu['total']/2
                jsonSave()
                print('영어점수가 변경되었습니다.!!')
            
            elif searchNo==0: # 상위메뉴이동
                print('상위메뉴로 이동합니다.')
            count=1 # 학생검색이 됨.
            break
    if count==0:    
        print('{} 학생이 없습니다.'.format(searchName))
        

# 학생삭제 함수        
def stu_delete():
    jsonRead() #학생생성리스트 호출 - stuSave
        
    print('학생성적 삭제를 선택하셨습니다.')
    searchName = input('삭제할 이름을 입력하세요.>>')
    count=0
    for i,stu in enumerate(stuSave):
        if searchName in stu.values():
            del(stuSave[i])
            print('{} 학생이 삭제되었습니다.'.format(searchName))
            count=1
            jsonSave()   # 학생리스트 파일저장
            break
    if count==0:
        print('{} 학생이 없습니다.'.format(searchName))   

# 학생성적 전체출력 함수       
def stu_print():
    jsonRead()  
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
        
# 학생검색 출력함수        
def stu_search():
    jsonRead()
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
        

# 학생등수 처리함수
def stu_rank():
    jsonRead()
    for stu in stuSave:
        rcount=1
        for stu2 in stuSave:
            if stu['total'] < stu2['total']: #total점수 비교
                rcount += 1    # stu2가 더 클경우 1증가
        stu['rank'] = rcount   # 등수입력        
    jsonSave()
    print('등수처리가 완료되었습니다.')                            


