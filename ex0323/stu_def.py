import os
import json
from logging import exception

stuSave=[]
count=0       # 학생검색 되었는지 체크하는 변수
# json읽기 함수
def jsonRead():
    stuSave = json.load(open('stuData.json','r'))

# json저장 함수
def jsonSave():
    json.dump(stuSave,open('stuData.json','w'))

# 학생번호 증가함수    
def stuCount():
    return stuSave[-1]['stuno']+1   


# 화면출력함수
def screen_print():
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
    return int(choice)

# 성적입력함수
def stu_input():
    # sCount = stuSave list개수+1
    jsonRead()
    print('-- {}번째 학생등록 -- '.format(stuCount()))
    sName = input('학생이름을 입력하세요.>>')
    kor = int(input('국어 점수를 입력하세요.>>'))
    eng = int(input('영어 점수를 입력하세요.>>')) 
    # 리스트 추가
    temp ={'stuno':sCount+1,'stuname':sName,'kor':kor,'eng':eng,\
        'total':kor+eng,'avg':(kor+eng)/2,'rank':0}
    stuSave.append(temp)
    print(stuSave)
    jsonSave()  # json저장함수 호출
    sCount += 1 #학생인원 count 1증가
    print('학생성적이 저장되었습니다.')
    return sCount

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


