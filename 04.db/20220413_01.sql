-- table타입확인
desc member;

-- ora_user 가지고 있는 table
select * from tab;

-- table부분 컬럼 출력
select id,password from member;

-- employees테이블 salary 월급
select salary from employees;

-- 월급, 주급, 월급*12개월 = 년봉 , 컬럼별칭선언
select salary, salary/5, salary*12 salary12  from employees;

-- order by : 순차정렬, order by desc : 역순정렬
select * from employees order by employee_id desc;

-- 최대값, 최소값 max, min
select max(employee_id) from employees;
select min(employee_id) from employees;

-- drop table member2;

select * from students;


select * from students;
-- 최대값에서 1증가후 출력
select max(stuid) from students;

-- max+1 증가 insert
insert into students values(
(select max(stuid)+1 from students),'홍길자',100,100,100,100+100+100,(100+100+100)/3,0);

select * from students;
rollback;

-- nvl함수 : null값일때 0으로 변경해서 계산
select id,name,nvl(total,0)+10 from member;


select commission_pct from employees;

-- 월급, 년봉, 
select emp_name,
salary*1230,salary*12*1230 as "Salary12",nvl(commission_pct,0),
(salary*12*1230) + (salary*12*1230*nvl(commission_pct,0)) as real_salary
from employees;

-- 밑변*높이*0.5
-- triangle 테이블 생성
create table triangle (
tno number(5) primary key,
base number(5,1),
height number(5,1),
area number(7,1)
);

-- 행추가
insert into triangle values(
4,35,12,35*12*0.5
);
commit;
select * from triangle;
-- 3개 15,4  20,9  35,12

select * from employees;
--사번,이름,이메일,전화번호,입사일 별칭을 사용해서 컬럼 5개 출력하시오.
select employee_id "사번",emp_name "이름",email "이메일",phone_number "전화번호",
hire_date "입사일" from employees;

select department_id "부서번호", department_name "부서명" from departments;

-- concatenation 연결
select * from employees;
select emp_name||'의 직급 :'|| job_id as jname from employees;

-- distinct 중복제거
select department_id,department_name from departments;
select distinct department_id from employees order by department_id;
select distinct job_id from employees;
select * from jobs;

select * from students;

-- where절 비교연산자 사용
select * from employees where employee_id>150;
select emp_name,salary from employees where salary>=3000 and salary<=7000
order by salary;

-- where절 검색 이름으로 검색
-- 소문자 변환-lower, 대문자 변환-upper, 첫글자 대문자 변환-initcap
select * from employees where lower(emp_name)='susan mavris' and 
upper(emp_name)='SUSAN MAVRIS' or initcap(emp_name)='Susan Mavris';

select * from employees where initcap(emp_name)='Susan Mavris';

-- 특정문자가 포함된 검색 like
select emp_name from employees 
where lower(emp_name) like '%ev%';

select department_id from employees where department_id=20;

-- 급여가 4000이하, 부서번호 30
select emp_name, department_id,salary from employees where salary<=4000
and department_id=30 order by salary;

select * from employees;

select email from employees where email>='PFAY';
-- 날짜검색
select hire_date from employees where hire_date='07/06/21';
select hire_date from employees where hire_date<='07/06/21';
-- 2000/01/01 이후 입사일인 사원을 출력하시오. 날짜 포맷지정
select to_char(hire_date,'YYYY/MM/DD') from employees where hire_date>='2000/01/01';

-- not검색
select * from employees where not department_id =10;
select * from employees where department_id != 10;
select * from employees where department_id <> 10;
select * from employees where department_id ^= 10;

-- 3000이상 7000이하 검색 출력
select salary from employees where salary>=3000 and salary<=7000
order by salary;

select salary from employees where salary between 3000 and 7000
order by salary;

select * from employees;

-- commission_pct 0.1 이거나 0.2 이거나 0.3
select commission_pct from employees
where commission_pct=0.1 or commission_pct=0.2 or commission_pct=0.3;


-- studata테이블 생성
create table studata (
	stuno number(4),
	stuname VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(5,2),
	avg number(5,2),
	rank number
);
insert into studata (stuno, stuname, kor, eng, math, total, avg, rank) values (1, 'McCullouch', 81, 99, 86, 266, 88.67, 0);

select * from studata;

commit;

-- 국어 90이상 영어 90이상 수학 90이상 학생출력
select * from studata
where kor>=90 and eng>=90 and math>=90;

-- 국어 90이상 100이하 학생출력
select * from studata
where kor>=80 and kor<=90;

select * from studata where kor not between 80 and 90;

-- 사원번호 120, 130, 140 인 사원을 출력하시오. employees
select * from employees
where employee_id =120 or employee_id=130 or employee_id=140;

-- in 연산자 : 동일한 필드 검색
select * from employees
where employee_id not in(120,130,140,150,160,170,180);

-- 사원번호가 130 이상이면서 salary 3000 이상 5000이하 사원을 출력하시오.
select employee_id,salary from employees
where employee_id>=130 and salary between 3000 and 5000 order by employee_id;

select * from employees
where  not (salary>=3000 and salary<=5000);

select * from employees
where not salary between 3000 and 5000;

select * from employees
where hire_date between '95/01/01' and '02/12/31' order by hire_date;

select hire_date,hire_date+1000 from employees;
-- 날짜데이터 사칙연산 가능, daul 가상테이블
select sysdate,sysdate+100 from Dual;

-- total 270,280,290 인 학생 출력 studata
select * from studata 
where total in (270,280,290);

select * from studata;

-- like 검색 %,_
select * from studata
where stuname like '%l%';
-- 대문자 S로 시작되는 학생검색
select * from studata
where stuname like 'S%';

-- 3자리에 l로 시작하는 학생검색
select * from studata
where stuname like '__l%';

-- 1. employees 끝자리 n으로 끝나는 사원출력
select * from employees
where emp_name like '%n';

-- 2. S,s 포함되어 있는 사원 출력
select * from employees
where emp_name like '%S%' or emp_name like '%s%';

select * from employees
where lower(emp_name) like '%s%';

-- 2번째 문자가 a가 포함되어 있는 학생검색
select * from employees
where emp_name not like '_a%';

-- null인 경우 검색 is null, is not null
select * from employees
where commission_pct is not null;

select * from member;

update member set total=null where id='aaa';

select * from member;

commit;

create table studata2 as
select * from studata;

select * from studata;
update studata2 set total=0;
update studata2 set avg=0;
commit;

update studata2 set total=kor+eng+math,avg=(kor+eng+math)/3;
update studata2 set avg=total/3;

-- 테이블삭제
-- drop table studata2;

-- 테이블 타입만 복제생성
create table studata2 as
select * from studata where 1=2;
select * from studata2;
desc studata2;

-- studata의 모든 컬럼데이터를 studata2에 복제
insert into studata2 
select * from studata;
select * from studata2;
delete studata2;
commit;

-- rank()함수 사용
select stuno, stuname,total,rank() over(order by total desc) rank
from studata;

-- studata의 일부 컬럼데이터를 studata2에 복제
insert into studata2(stuno,stuname,kor,eng,math,total,avg,rank)
select stuno,stuname,kor,eng,math,total,avg,
rank() over (order by total desc) rank 
from studata;

select * from studata2;
select * from studata2 order by stuno;

select employee_id from employees;

-- order by 정렬 asc순차정렬, desc 역순정렬
select salary from employees order by salary;
select salary from employees order by salary desc;

-- employees2테이블 : employee_id, emp_name, salary, rank
-- employees의 모든 데이터를 employees2에 넣을 것. salary를 가지고 rank할것

-- employees2테이블 : employee_id, emp_name, salary
create table employees2 as
select employee_id,emp_name,salary from employees where 1=2;

-- rank컬럼 추가
alter table employees2 add rank number(4);
desc employees2;

-- employees의 데이터 rank포함 employees2에 복사
insert into employees2
select employee_id,emp_name,salary,
rank() over (order by salary desc) 
from employees order by salary desc;

commit;
select * from employees2 order by employee_id;

delete employees2;

select employee_id,emp_name,salary,
rank() over (order by salary desc)
from employees;

-- 부서번호 순차정렬, 월급 역순정렬
select department_id,salary from employees
order by department_id,salary desc;

select employee_id,department_id,hire_date from employees
order by employee_id asc,department_id asc,hire_date desc;

--abs함수:절대값
select -10,abs(-10) from dual;

-- 소수점 버림
select floor(10.3456) from dual;
-- 반올림, 해당 소수점 자리수까지 표현
select round(10.4567,3) from dual;
-- 정수 첫째자리에서 반올림
select round(277.4567,-1) from dual;

select * from studata;

--mod나머지: 학번이 홀수 번호만 출력
select * from studata
where mod(stuno,2)=1;

-- 사원번호가 짝수 번호만 출력하시오.
select * from employees
where mod(employee_id,2)=0 order by employee_id;

-- 
drop table employees2;

-- employees2 table생성 employee_id, emp_name,salary,rank 사원번호가 홀수 인것만 
-- 추가해서 테이블 생성해보세요.
-- employees의 데이터 rank포함 employees2에 복사
insert into employees2
select employee_id,emp_name,salary,
rank() over (order by salary desc) rank
from employees
where mod(employee_id,2)=1
order by salary desc
;

select * from employees2 order by employee_id;
--delete employees2;
commit;

select * from students;
insert into students values
(
(select max(stuid)+1 from students),'이유신',100,100,100,300,100,0);

--시퀀스 생성

create table students2 as
select * from students where 1=2;

select * from students2;

-- nextval : 시퀀스 다음 번호를 가져옴. currval : 현재 번호를 가져옴.
insert into students2 values(
board_seq.nextval,'김유신',100,100,100,(100+100+100),(100+100+100)/3,0);

select board_seq.currval from dual;

select board_seq.nextval from dual;

-- 시퀀스 이름 설정 
CREATE SEQUENCE test_seq
INCREMENT BY 1
 START WITH 1 
MINVALUE 1
MAXVALUE 9999999 
cycle
cache 10;

create sequence emp_seq
increment by 1
 start with 1
maxvalue 100000
;

-- emp01 테이블 생성 
-- empno number(5) - 99999, employee_id, emp_name,salary
-- empno emp_seq생성해서 추가, 나머지 컬럼 employees의 내용을 입력하시오.
create table emp01 as
select employee_id,emp_name,salary from employees where 1=2;
select * from emp01;
-- 
alter table emp01 add empno number(5);


insert into emp01
select employee_id,emp_name,salary,emp_seq.nextval from employees;

select * from emp01;

-- emp02 empno,employee_id,emp_name,salary 
-- emp01에서 데이터 복사

alter table emp01 modify emp_name invisible;
alter table emp01 modify employee_id invisible;
alter table emp01 modify salary invisible;

alter table emp01 modify emp_name visible;
alter table emp01 modify employee_id visible;

select * from emp01;















