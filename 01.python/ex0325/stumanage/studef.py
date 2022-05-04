from stumanage.student import Student
from stumanage.stuOracle import *


# 학생저장 전역변수 선언
stuSave=[]

# 화면출력
def screenPrint():
    print('[ 학생성적프로그램 ]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('3. 학생검색출력')
    print('4. 학생성적수정')
    print('5. 학생성적삭제')
    print('6. 학생등수처리')
    print('0. 프로그램종료')
    print()
    choice = int(input('원하는 번호를 입력하세요.>>'))
    
    return choice

# 학생성적입력
def stuInput():
    conn = myConn() # db연결
    cs = conn.cursor() #메모리선언
    while True:
        print('[ 학생성적입력 ]')
        stuname = input('학생이름을 입력하세요.(0.종료)>>')
        if stuname=='0':
            break
        kor = int(input('국어점수를 입력하세요.>>'))
        eng = int(input('영어점수를 입력하세요.>>'))
        # 객체선언후 리스트에 저장
        temp = Student(stuname,kor,eng)
        stuSave.append(temp)
        print('{}번.{} 학생이 저장되었습니다.'.format(temp.stuno,stuname))
        print()

# 상단타이틀 출력
def topTitle():
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
    print('-'*60)

# 학생전체출력        
def stuoutput():
    topTitle()
    for stu in stuSave:
        print(stu) 
        
# 학생검색출력 - eq
def stusearch():
    print()
    print('[ 학생검색출력 ]')
    sname = input('학생이름을 입력하세요.>>')
    count=0
    for stu in stuSave:
        if stu == sname:
            topTitle()
            print(stu) 
            count=1
            break
    
    if count == 0:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.!!')                         
        
        
# 학생성적수정 
def stuModify():
    print()
    print('[ 학생성적수정 ]')
    sname = input('학생이름을 입력하세요.>>')
    count=0
    for stu in stuSave:
        if stu == sname:
            print('{} 학생이 검색되었습니다.'.format(sname)) 
            print('[성적수정]')
            print('1. 국어점수')
            print('2. 영어점수')
            tempNum = int(input('수정과목 번호를 입력하세요.>>'))
            if tempNum == 1:
               print('현재 국어점수 : {}'.format(stu.kor))
               score = int(input('수정할 점수를 입력하세요.>>'))
               stu.setKor(score)
               print('국어점수가 {}으로 변경되었습니다.'.format(score))
            elif tempNum == 2:
               print('현재 영어점수 : {}'.format(stu.eng))
               score = int(input('수정할 점수를 입력하세요.>>'))
               stu.setEng(score)    
               print('영어점수가 {}으로 변경되었습니다.'.format(score))
            count=1
            break
    
    if count == 0:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.!!') 

# 학생성적 삭제               
def stuDelete():
    print()
    print('[ 학생성적삭제 ]')
    sname = input('학생이름을 입력하세요.>>')
    count=0
    for i,stu in enumerate(stuSave):
        if stu == sname:
            print('{} 학생이 검색되었습니다.'.format(sname)) 
            flag = input('정말 삭제하시겠습니까?')
            if flag == 'y' or flag =='Y':
               del(stuSave[i])
               print('{} 학생이 삭제되었습니다.'.format(sname))
            else:
               print('삭제가 최소되었습니다.')
            count=1
            break
    
    if count == 0:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.!!')
        
# 학생등수처리        
def sturank():
    for stu1 in stuSave:
        rankCount=1
        for stu2 in stuSave:
            if stu1<stu2:   # 클래스 __lt__자동호출
                rankCount += 1
        stu1.rank = rankCount
    print('등수처리가 완료되었습니다.!')
    print()                            