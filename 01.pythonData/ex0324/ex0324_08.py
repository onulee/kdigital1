from exstudent import Student



stuno = int(input('학생번호를 입력하세요.>>'))
stuname = input('학생이름을 입력하세요.>>')
kor = int(input('국어점수를 입력하세요.>>'))
eng = int(input('영어점수를 입력하세요.>>'))
s1 = Student(stuno,stuname,kor,eng)


print('{},{},{},{},{},{},{}'.format(s1.stuno,s1.stuname,s1.kor,s1.eng,\
    s1.total,s1.avg,s1.rank))