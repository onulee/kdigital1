select * from tab;

--drop table emp02;

-- drop table employees2;

--drop table students2;

--rename studata2 to sturank;

select * from board;
select * from membership;

insert into board values(
board_seq.nextval,'abc','이벤트 진행합니다.','이벤트 경품을 진행합니다.',sysdate,1);

create table emp02(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2) check(deptno between 10 and 19),
gender char(1) check(gender in('M','F'))
);
insert into emp02 values(
emp_seq.nextval,'홍길동','manager',10,'M');

insert into emp02 values(
emp_seq.nextval,'홍길자','manager',10,'F');

insert into emp02 values(
emp_seq.nextval,'홍길순','manager',18,'F');

insert into emp02 values(
emp_seq.nextval,'홍길순','manager',18,'A');

select * from emp02;

select emp_seq.currval from dual;

desc emp02;

--drop table emp02;

--drop table emp01;

--employees테이블을 참조하여 emp01 테이블 생성
--employees
--employee_id primary key
--emp_name unique
--salary not null
--manager_id
--department_id
-- 107개의 데이터를 입력하시오.

create table emp01(
employee_id number(6) primary key,
emp_name varchar2(80) unique,
salary number(8,2) not null,
manager_id number(6),
department_id number(6)
);

insert into emp01
select employee_id,emp_name,salary,manager_id,department_id from employees;

-- foregin key 등록
-- 선언 : idex명 mem_fk_id, 외래키(컬럼) 위치 membership테이블 id
--constraint mem_fk_id foreign key(id) references membership(id)
alter table emp01
add constraint departments_fk_id foreign key(department_id) 
references departments(department_id);

--primary key 삭제
alter table emp01 drop primary key;

--primary key 생성
alter table emp01 add primary key(employee_id);

select * from students;

select * from studata;

select * from membership;

select * from sturank order by stuno;
--sturank의 stuname을 fk로 등록 membership id
--1. membership id primary key 등록
--alter table membership add primary key(id);
--2. sturank fk 등록
alter table sturank
add constraint sturank_fk_id foreign key(stuname) references membership(id);

-- 테이블 컬럼 이름 변경
alter table sturank rename column stuname to id;
--update sturank set stuname='eee' where stuno=5;
-- delete sturank where stuno>5;

select * from employees;

select emp_name,department_id,
decode(department_id,
20,'승진대상',30,'승진보류',
40,'승진보류',
50,'승진보류') "승진확인" 
from employees;

select * from students;
select stuid,stuname,avg,decode(avg,100,'만점') as "상태"
from students;

select job_id from employees;

-- sh clerk salary*2% , ad asst 5%인상, it prog 3%, pu_clerk 4%
-- 월급을 인상해서 출력하시오.
-- employee_id,emp_name, salary, job_id, "월급인상현황"
select employee_id,emp_name,job_id,salary,
decode(job_id,
'SH_CLERK',salary*0.02,
'AD_ASST',salary*0.05,
'IT_PROG',salary*0.03,
'PU_CLERK',salary*0.04
) as "월급인상현황" from employees;


-- CLERK, MAN, REP, ACCOUNT
select employee_id,emp_name,job_id,salary,
decode(substr(job_id,4),
'CLERK',salary*0.05,
'MAN',salary*0.07,
'REP',salary*0.04,
'ACCOUNT',salary*0.06
) as "월급인상현황" from employees;








