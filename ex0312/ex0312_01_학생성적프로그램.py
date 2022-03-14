# 번호,이름,국어,영어,합계,평균,등수 - 10명의 학생입력공간 생성

stuSave = [[0]*7 for _ in range(10)]
# print(stuSave)
# 학생가입인원 확인count
sCount = 0
while True:
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('0. 프로그램종료')
    print('-'*25)
    choice = int(input('원하는 번호를 입력하세요.>>'))
    
    if choice==1:
        print('-- {}번째 학생등록 -- '.format(sCount+1))
        sName = input('학생이름을 입력하세요.>>')
        kor = int(input('국어 점수를 입력하세요.>>'))
        eng = int(input('영어 점수를 입력하세요.>>')) 
        stuSave[sCount][0] = sCount+1  # 학생번호 입력
        stuSave[sCount][1] = sName
        stuSave[sCount][2] = kor
        stuSave[sCount][3] = eng
        stuSave[sCount][4] = kor+eng
        stuSave[sCount][5] = (kor+eng)/2  #float
        sCount += 1 #학생인원 count 1증가
        print('학생성적이 저장되었습니다.')
        print(stuSave)
        
        
    elif choice==2:
        print('학생성적 수정을 선택하셨습니다.')
    elif choice==3:
        print('학생성적 삭제를 선택하셨습니다.')
    elif choice==0:
        print('프로그램을 종료합니다.')
        break