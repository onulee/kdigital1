id='admin'
pw='1111'

while True:
    u_id = input('아이디를 입력하세요.>>')
    u_pw = input('패스워드를 입력하세요.>>')

    if(id==u_id and pw==u_pw):
        stu_no = input('학생번호를 입력하세요.>>')
        stu_name = input('학생이름을 입력하세요.>>')
        kor = int(input('국어점수를 입력하세요.>>'))
        eng = int(input('영어점수를 입력하세요.>>'))
        math = int(input('수학점수를 입력하세요.>>'))
        print('학생번호 : '+stu_no)
        print('학생이름 : '+stu_name)
        print('국어 :',kor)
        print('영어 :',eng)
        print('수학 :',math)
        print('합계 : {}'.format(kor+eng+math))
        print('평균 : {:.2f}'.format((kor+eng+math)/3))
    else:
        print('아이디,패스워드가 일치하지 않습니다. 프로그램을 종료합니다.')

# # 입력
# a= input()
# # 출력
# print(a)