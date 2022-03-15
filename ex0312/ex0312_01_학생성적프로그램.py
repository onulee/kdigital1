# 번호,이름,국어,영어,합계,평균,등수 - 10명의 학생입력공간 생성

# stuSave = [[0]*7 for i in range(0)]
stuSave = []
# print(stuSave)
# 학생가입인원 확인count
sCount = 0
while True:
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생성적전체출력')
    print('0. 프로그램종료')
    print('-'*25)
    choice = int(input('원하는 번호를 입력하세요.>>'))
    
    if choice==1:
        print('-- {}번째 학생등록 -- '.format(sCount+1))
        sName = input('학생이름을 입력하세요.>>')
        kor = int(input('국어 점수를 입력하세요.>>'))
        eng = int(input('영어 점수를 입력하세요.>>')) 
        
        temp =[sCount+1,sName,kor,eng,kor+eng,(kor+eng)/2,0]
        stuSave.append(temp)
        sCount += 1 #학생인원 count 1증가
        print('학생성적이 저장되었습니다.')
        print(stuSave)
    elif choice==2:
        print('학생성적 수정을 선택하셨습니다.')
    elif choice==3:
        print('학생성적 삭제를 선택하셨습니다.')
    elif choice==4:
        print('번호\t이름\t국어\t영어\t합계\t평균\t등수')  
        # print('{:10s}{:10s}{:10s}{:10s}{:10s}{:10}{:10s}'.format('번호','이름',\
        #     '국어','영어','합계','평균','등수'))  
        print('-'*45)
        # [[1,홍길동,100,100,200,100.0,0]]
        for stu in stuSave:
            for i in stu:
               print('{}\t'.format(i),end='') 
            print() #줄바꿈  
                
    elif choice==0:
        print('프로그램을 종료합니다.')
        break