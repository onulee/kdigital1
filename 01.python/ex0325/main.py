# 학생관리폴더 - 학번,이름,전화번호,주소,성별,학년,학과
# 학생성적폴더 - 학번,국어,영어,수학,합계,평균,등수
# from stumanage.student import Student
from stumanage.studef import *

# 프로그램 시작
while True:
    #화면출력
    choice = screenPrint()

    if choice==1:
        stuInput()    # 학생성적입력
        
    elif choice == 2:
        stuoutput()   # 학생전체출력 
        
    elif choice == 3:
        stusearch()   # 학생검색출력 
           
    elif choice == 4:
        stuModify()   # 학생성적수정 
           
    elif choice == 5:
        stuDelete()   # 학생성적삭제 
           
    elif choice == 6:
        sturank()     # 학생등수처리   
        
    else:
        print('프로그램을 종료합니다.!')
        break     
        
    


