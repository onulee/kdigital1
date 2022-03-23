# 번호,이름,국어,영어,합계,평균,등수 - 10명의 학생입력공간 생성
# stuSave = [[0]*7 for i in range(0)]
# import stu_def          #모듈선언
# import stu_def as stu   #모듈선언후 별칭사용
from stu_def import *
import json

while True:
    choice=0  #화면출력 선택번호변수
    choice = screen_print()  # 화면출력함수 호출
    
    if choice==1: # 학생성적입력
        # 학생성적입력함수 호출 
        sCount = stu_input()
    elif choice==2:
        # 학생성적 수정 호출
        stu_modify()
        
    elif choice==3:
        stu_delete() #학생성적 삭제호출
        
    elif choice==4:
        stu_print()  # 학생성적 전체출력 호출
        
    elif choice==5:
        stu_search() # 학생검색 출력 호출
    
    elif choice==6:
        stu_rank()   # 학생등수처리 호출
                
    elif choice==0:
        print('프로그램을 종료합니다.')
        break