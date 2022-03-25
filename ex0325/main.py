# 학생관리폴더 - 학번,이름,전화번호,주소,성별,학년,학과
# 학생성적폴더 - 학번,국어,영어,수학,합계,평균,등수

from stumanage.student import Student


s = Student(1,'홍길동',100,100)

s.setKor(-100)
s.kor=-100

print('{},{}'.format(s.stuname,s.kor))