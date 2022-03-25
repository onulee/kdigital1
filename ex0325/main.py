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
        
    


