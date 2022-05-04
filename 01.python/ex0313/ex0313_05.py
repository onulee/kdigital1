# 1- 이름을 검색해서 삭제를 하는 프로그램을 만드시오.

# 1. 찾는 사람 검색
# 2. 찾는 사람 삭제
# 원하는 번호를 입력하세요.>>

students=[
    [1,'홍길동',100,100,200,100.0,0],
    [2,'이순신',100,100,200,100.0,0],
    [3,'유관순',100,100,200,100.0,0],
    [4,'김유신',100,100,200,100.0,0],
    [5,'김구',100,100,200,100.0,0]
]

while True:
    print('1. 찾는 사람 검색')
    print('2. 찾는 사람 삭제')
    choice = int(input('원하는 번호를 입력하세요.>>')) 
    chk=0

    if choice==1:
       chkname = input('찾는 학생이름을 입력하세요.>>') 
       for stu in students:
           if chkname in stu:
               print(stu)
               print()
               chk=1
               break
       if chk==0:
          print('찾는 학생이 없습니다. 다시 입력해주세요.!!!')        
        
    elif choice == 2:
        chkname = input('삭제할 학생이름을 입력하세요.>>') 
        for i,stu in enumerate(students):
           if chkname in stu:
               del(students[i])
               # 전체학생 출력
               print(students) 
               chk=1
               break
        if chk==0:
           print('삭제할 학생이 없습니다. 다시 입력하세요.!!!')          
        
    