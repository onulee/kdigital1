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
    
def myInsert():
    conn = myConn() # db연결함수 호출
    cs = conn.cursor() 
    sql="insert into studata values (stu_seq.nextval,'홍길동',100,100,92,100+100+92,(100+100+92)/3,1)"
    rows = cs.execute(sql)
    print("insert : ",cs.rowcount)
    cs.close()
    conn.commit()
    conn.close()
    

## 프로그램 실행 ##
mySelect()
myInsert() # 1개 데이터 추가

    
  