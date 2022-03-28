import student

stuSave=[]
while True:
    sCount = int(input('학생번호를 입력하세요.(0.종료)>>'))
    if sCount==0:
        break
    sName = input('이름을 입력하세요.>>')
    kor = int(input('국어점수를 입력하세요.>>'))
    eng = int(input('영어점수를 입력하세요.>>'))
    stuSave.append(student.Student(sCount,sName,kor,eng))

# 홍길동,이순신
tempName = input('홍길동의 이름을 변경하세요.>>')
stuSave[0].setStuname(tempName)

temp = int(input('홍길동의 국어점수를 변경하세요.>>'))
# student.Student.setKor(temp)
stuSave[0].setKor(temp)
# stuSave[0].kor=-100
# s3 = student.Student(3,'유관순',100,100)
# s3.setKor(90)


print('번호','이름','국어','영어','합계','평균','등수',sep='\t')    
for stu in stuSave:
   print(stu) 
         

