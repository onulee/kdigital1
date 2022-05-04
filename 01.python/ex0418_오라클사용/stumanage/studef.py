from stumanage.student import Student
from stumanage.stuOracle import *
import cx_Oracle

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
    while True:
        print('[ 학생성적입력 ]')
        stuname = input('학생이름을 입력하세요.(0.종료)>>')
        if stuname=='0':
            break
        kor = int(input('국어점수를 입력하세요.>>'))
        eng = int(input('영어점수를 입력하세요.>>'))
        math = int(input('수학점수를 입력하세요.>>'))
        
        # insert 함수 호출
        myInsert(stuname,kor,eng,math)
        print()

# 상단타이틀 출력
def topTitle():
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)

# 학생전체출력        
def stuoutput():
    topTitle()  # 상단제목 출력함수호출
    mySelect()  # 오라클 전체 select, 개수 count
    print()
    
# 학생검색출력 - eq
def stusearch():
    print('[ 학생검색출력 ]')
    search_name = input('학생이름을 입력하세요.>>')
    # select 검색으로 db호출
    mySelectOne(search_name)
        
        
# 학생성적수정 
def stuModify():
    myUpdate() # 업데이트 호출
    

# 학생성적 삭제               
def stuDelete():
    myDelete() # 삭제함수 호출
    
        
# 학생등수처리        
def sturank():
    myRank()
    # for stu1 in stuSave:
    #     rankCount=1
    #     for stu2 in stuSave:
    #         if stu1<stu2:   # 클래스 __lt__자동호출
    #             rankCount += 1
    #     stu1.rank = rankCount
    # print('등수처리가 완료되었습니다.!')
    # print()                            