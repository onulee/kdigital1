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

print('번호','이름','국어','영어','합계','평균','등수',sep='\t')    
for stu in stuSave:
   print(stu) 
         

