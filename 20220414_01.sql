select * from studata2;

-- employees2 시퀀스번호,사원번호,사원명,직급, 입사일 테이블 생성
-- employees 107명 추가
-- 입사일 오름차순 기준으로 출력하시오.

create table employees2 as
select employee_id,emp_name,job_id,hire_date from employees
where 1=2;

alter table employees2 add seqno number(4);

insert into employees2
select employee_id,emp_name,job_id,hire_date,emp_seq.nextval
from employees;

commit;

select * from employees2;

create sequence emp_seq
 start with 1
 increment by 1
 minvalue 1
 maxvalue 9999
 nocycle
 nocache;
 
-- 컬럼순서 변경방법 
-- 테이블 컬럼 숨김
alter table employees2 modify HIRE_DATE invisible;

-- 테이블 컬럼 보임
alter table employees2 modify HIRE_DATE visible;

-- seqno,employee_id,emp_name,job_id,hire_date
-- emp_name,job_id,hire_date,seqno,employee_id
select * from employees2;
desc employees2;

select * from employees;

-- 문자함수 : upper대문자 , lower소문자, initcap첫글자대문자
select upper(emp_name) from employees;
select lower(emp_name) from employees;
select initcap(emp_name) from employees;

-- 문자길이: 영문,한글공통 length
select emp_name,length(emp_name),lengthb(emp_name) from employees;
select stuname,length(stuname),lengthb(stuname) from students;

-- 문자열 추출: substr
select emp_name,substr(emp_name,0,6) from employees;
select emp_name,substr(emp_name,7) from employees;
select emp_name,substr(emp_name,-1) from employees;

--컬럼추가
alter table member add filename varchar2(20);

select * from member;

-- 컬럼수정
update member set password='5555',juminno='000912-3103212'
where id='eee';
update member set filename='bbb.doc'
where id='eee';

commit;

select name,substr(juminno,0,6) "주민번호앞자리",substr(juminno,8) "주민번호뒤자리"
from member;

select name,juminno,substr(juminno,0,8)||'******' juminno2,
length(substr(juminno,0,8)||'******') ju_length 
from member;

-- *.hwp, *.xls, *.pdf, *.csv

-- member테이블
-- id의 길이, juminno 앞자리, jiminno뒤자리, filename 뒤에서 3자리 출력하시오.










