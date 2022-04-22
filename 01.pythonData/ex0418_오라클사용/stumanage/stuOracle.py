import cx_Oracle

# db연결 함수
def myConn():
    # db 연결
    conn = cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
    return conn

# insert 함수 호출    
def myInsert(stuname,kor,eng,math):
    conn = myConn() # db연결함수 호출
    cs = conn.cursor() 
    
    sql="insert into studata values (stu_seq.nextval,:1,:2,:3,:4,:5,:6,1)"
    # 입력받은 데이터를 저장
    cs.execute(sql,(stuname,kor,eng,math,kor+eng+math,(kor+eng+math)/3))
    print()
    print('{} 학생 {}명의 데이터가 저장되었습니다.'.format(stuname,cs.rowcount))
    cs.close()
    conn.commit()
    conn.close()


# 전체 select 함수호출
def mySelect():
    conn = myConn() # db연결함수 호출
    # db실행후 저장공간 메모리 선언
    cs = conn.cursor() 
    # sql구문 실행
    sql = "select * from studata order by stuno"
    # sql = "select * from studata where stuname like '%홍길자%'"
    rows = cs.execute(sql)
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')
        # print(row)
    print()
    print("{}의 데이터가 검색되었습니다.".format(cs.rowcount))    
    # 1개의 row데이터 가져오는 방법    
    # sql="select count(*) count from studata"
    # cs.execute(sql)
    # count = cs.fetchone()  # select 1개 데이터 가져오기
    # print("{}의 데이터가 검색되었습니다.".format(count[0]))
    print()    
    cs.close()
    conn.close() 
    
# 1개 이름으로 검색, select 함수호출
def mySelectOne(search_name):
    conn = myConn() # db연결함수 호출
    # db실행후 저장공간 메모리 선언
    cs = conn.cursor() 
    # sql구문 실행
    sql = "select * from studata where stuname like '%"+search_name+"%'"
    cs.execute(sql)
    # cs.fetchall() -> list타입, cs.fetchone -> 1개
    # select count(*) from studata
    rows = cs.fetchall() #모든 데이터를 가져옴. list타입으로 반환
    if(len(rows) != 0): # list개수가 0인지 확인
        for row in rows:
            print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')
            # print(row)
        print()
        print("{}의 데이터가 검색되었습니다.".format(cs.rowcount))   
    else:
        print("찾는 데이터가 없습니다. 다시 검색하세요.!")    
        print()
    cs.close()
    conn.close() 
    
    
## update함수 호출    
def myUpdate():
    conn = myConn() # db연결함수 호출
    # db실행후 저장공간 메모리 선언
    cs = conn.cursor() 
    # sql구문 실행
    print('[ 학생성적수정 ]')
    search_name = input('학생이름을 입력하세요.>>')
    sql = "select * from studata where stuname='"+search_name+"'"
    print("sql : ",sql)
    cs.execute(sql)
    rows = cs.fetchall()
    # rows의 개수
    if len(rows) != 0:   # 검색된 이름이 없는 경우
        for row in rows:
            if row[1] == search_name:
                print('{} 학생이 검색되었습니다.'.format(search_name)) 
                print('[성적수정]')
                print('1. 국어점수')
                print('2. 영어점수')
                tempNum = int(input('수정과목 번호를 입력하세요.(0.종료)>>'))
                if tempNum == 1:
                    print('현재 국어점수 : {}'.format(row[2]))
                    score = int(input('수정할 점수를 입력하세요.>>'))
                    sql="update studata set kor=:0,total=:1,avg=:2 where stuname=:3"
                    cs.execute(sql,(score,(score+row[3]+row[4]),(score+row[3]+row[4])/3,search_name))
                    cs.close()
                    conn.commit()
                    conn.close()
                    print('국어점수가 {}으로 변경되었습니다.'.format(score))
                elif tempNum == 2:
                    print('현재 영어점수 : {}'.format(row[3]))
                    score = int(input('수정할 점수를 입력하세요.>>'))
                    sql="update studata set eng=:1,total=:2,avg=:3 where stuname=:4"
                    # 입력받은 데이터를 저장
                    cs.execute(sql,(score,(row[2]+score+row[4]),(row[2]+score+row[4])/3,search_name))
                    print("update : ",cs.rowcount)
                    cs.close()
                    conn.commit()
                    conn.close()
                    print('{} 학생의 영어점수가 {}으로 변경되었습니다.'.format(search_name,score))
                    count=1
                    break
                elif tempNum == 0:
                    break
    else:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.!!')
    
    
## delete함수 호출    
def myDelete():
    conn = myConn()
    cs = conn.cursor()
    print('[ 학생성적삭제 ]')
    search_name = input('학생이름을 입력하세요.(0.종료)>>')
    # sql구문 실행
    sql = "select * from studata where stuname like '%"+search_name+"%'"
    cs.execute(sql)
    rows = cs.fetchall() #모든 데이터를 가져옴. list타입으로 반환
    if(len(rows) != 0): # 검색 후, list개수가 0인지 확인
        print("[ 검색된 학생목록 ]")
        for row in rows:
            print("삭제번호 :",row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')
            # print(row)
        # 찾은 데이터에서 삭제할 번호 선택    
        print('{} 학생이 검색되었습니다.'.format(search_name)) 
        flag = input('삭제할 번호를 입력하세요.(0.삭제취소) >> ')
        if flag != '0':
            sql="delete from studata where stuno="+flag
            cs.execute(sql)
            print('학생이 삭제되었습니다.')
        else:
            print('삭제가 최소되었습니다.')
    else:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.!!')
    
    print("delete : ",cs.rowcount)
    cs.close()
    conn.commit()
    conn.close() 
    
    
## rank 등록함수 호출    
def myRank():
    conn = myConn()
    cs = conn.cursor()
    print('[ 학생등수처리 ]')
    num = input('학생등수처리를 진행할까요?(0.종료) >> ')
    # sql구문 실행
    sql = "update studata a set rank=(select ranks from \
(select rank() over(order by total desc) as ranks,stuno from studata) b where b.stuno = a.stuno)"
    cs.execute(sql)
    print("rank : ",cs.rowcount)
    print('등수처리가 완료되었습니다.')
    cs.close()
    conn.commit()
    conn.close() 
    

    
  