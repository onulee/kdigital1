from stumanage.student import Student

# 학생저장 전역변수 선언
stuSave=[]

# 화면출력
def screenPrint():
    print('[ 학생성적프로그램 ]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('3. 학생검색출력')
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
        # 객체선언후 리스트에 저장
        temp = Student(stuname,kor,eng)
        stuSave.append(temp)
        print('{}번.{} 학생이 저장되었습니다.'.format(temp.stuno,stuname))
        print()

# 학생전체출력        
def stuoutput():
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
    print('-'*60)
    for stu in stuSave:
        print(stu)                