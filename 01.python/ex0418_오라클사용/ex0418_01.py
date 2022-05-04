import cx_Oracle

# db연결 함수
def myConn():
    # db 연결
    conn = cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
    return conn

# select 함수호출
def mySelect():
    conn = myConn() # db연결함수 호출
    # db실행후 저장공간 메모리 선언
    cs = conn.cursor() 
    # sql구문 실행
    rows = cs.execute("select * from studata")
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)
    for row in rows:
        # print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')
        print(row)
    cs.close()
    conn.close() 
   
# insert 함수 호출    
def myInsert():
    conn = myConn() # db연결함수 호출
    cs = conn.cursor() 
    # 데이터 입력받음.
    print('[ 학생성적입력 ]')
    stuname = input('학생이름을 입력하세요.(0.종료)>>')
    kor = int(input('국어점수를 입력하세요.>>'))
    eng = int(input('영어점수를 입력하세요.>>'))
    math = int(input('수학점수를 입력하세요.>>'))
    
    sql="insert into studata values (stu_seq.nextval,:1,:2,:3,:4,:5,:6,1)"
    # 입력받은 데이터를 저장
    cs.execute(sql,(stuname,kor,eng,math,kor+eng+math,(kor+eng+math)/3))
    print("insert : ",cs.rowcount)
    cs.close()
    conn.commit()
    conn.close()
    
## update함수 호출    
def myUpdate():
    conn = myConn()
    cs = conn.cursor()
    print('[ 학생성적수정 ]')
    stuname = input('학생이름을 입력하세요.(0.종료)>>')
    kor = int(input('국어점수를 입력하세요.>>'))   
    eng = int(input('영어점수를 입력하세요.>>'))  
    math = int(input('수학점수를 입력하세요.>>')) 
    sql="update studata set kor=:1,eng=:2,math=:3,total=:4,avg=:5 where stuname=:6"
    # 입력받은 데이터를 저장
    cs.execute(sql,(kor,eng,math,(kor+eng+math),(kor+eng+math)/3,stuname))
    print("update : ",cs.rowcount)
    cs.close()
    conn.commit()
    conn.close() 
    
## delete함수 호출    
def myDelete():
    conn = myConn()
    cs = conn.cursor()
    print('[ 학생성적삭제 ]')
    stuname = input('학생이름을 입력하세요.(0.종료)>>')
    sql="delete studata where stuname='"+stuname+"'"
    # sql="delete from studata where stuno=:1 and stuname=:2"
    # 입력받은 데이터를 저장
    cs.execute(sql)
    print("delete : ",cs.rowcount)
    cs.close()
    conn.commit()
    conn.close() 
    
    
    

## 프로그램 실행 ##
mySelect()
# myInsert() # 데이터 추가
# myUpdate() # 데이터 수정
myDelete() #데이터 삭제

    
  