id='admin'
pw='1111'
students=[]
count=1
# u_id = input('아이디를 입력하세요.>>')
# u_pw = input('패스워드를 입력하세요.>>')
# 무한반복
while True:
    stu_no = count
    print('학생번호 :',stu_no)
    stu_name = input('학생이름을 입력하세요.>>')
    kor = int(input('국어점수를 입력하세요.>>'))
    eng = int(input('영어점수를 입력하세요.>>'))
    math = int(input('수학점수를 입력하세요.>>'))
    total = kor+eng+math
    avg = total/3
    rank = 0
    student = [stu_no,stu_name,kor,eng,math,total,avg,rank]
    students.append(student)
    print(students)
    count += 1


# # 입력
# a= input()
# # 출력
# print(a)