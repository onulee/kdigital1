from student import Student

# 학생저장 전역변수 선언
stuSave=[]

# 화면출력
def screenPrint():
    print('[ 학생성적프로그램 ]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적출력')
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
        kor = int(input('학생이름을 입력하세요.>>'))
        eng = int(input('학생이름을 입력하세요.>>'))
        # 객체선언후 리스트에 저장
        stuSave.append(Student(stuname,kor,eng))
        print('{} 학생이 저장되었습니다.'.format(stuname))
        print()