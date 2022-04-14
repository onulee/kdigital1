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
update member set password='    5555   ',juminno='  000912-3103212   '
where id='eee';
update member set filename='   bbb.doc'
where id='eee';

--컬럼추가
insert into member values(
'hhh','   7777','홍길영     ','010-   9999-9999',300,100,'910101-1100123','  gkhtkd  .html');

commit;

select name,substr(juminno,0,6) "주민번호앞자리",substr(juminno,8) "주민번호뒤자리"
from member;

select name,juminno,substr(juminno,0,8)||'******' juminno2,
length(substr(juminno,0,8)||'******') ju_length 
from member;

-- *.hwp, *.xls, *.pdf, *.csv

-- member테이블
-- id의 길이, juminno 앞자리, jiminno뒤자리, filename 뒤에서 3자리 출력하시오.
select id,length(id),substr(juminno,0,6),substr(juminno,8),
substr(filename,-3) from member;

-- 특정문자 위치 찾기(instr)
select filename,instr(filename,'.'),substr(filename,instr(filename,'.')+1) from member;

-- replace 문자대체함수
select emp_name from employees;
select replace(emp_name,' ','') from employees;

-- trim,ltrim,rtrim 공백제거함수
select password,length(password), ltrim(password) from member;
select phone,length(phone) from member;
select filename,length(filename),ltrim(filename),length(ltrim(filename)) from member;

update member set filename=ltrim(filename);

update member set phone=replace(phone,' ','');
update member set phone='010-9999-9999';

select * from member;

-- concat 문자열 합치기
select concat(id,concat('-',password)) as juminno from member;
-- 연결연산자
select id||'-'||password as juminno from member;

-- 빈공간 특정문자 채우기 (lpad,rpad)
select rpad(id,10,'*') from member;

select juminno from member;
select rpad(substr(juminno,0,8),14,'*')as juminno from member;


-- 현재날짜함수
select sysdate-1,sysdate,sysdate+1 from dual;

select * from member;

select * from emp01;

alter table member add create_date date;

insert into member(id,password,create_date) values(
'iii','1111',sysdate);

select to_char(create_date,'YYYY-MM-DD hh:mi:ss') from member;
select create_date from member;


select hire_date from employees;

-- 소수점 삭제
select trunc(sysdate-to_date('22/03/08')) from dual;

-- 월 반올림
select hire_date, round(hire_date,'month') from employees;

-- 일자 반올림
select round(create_date,'ddd') from member;

-- 개월 추가 months_between
select sysdate,add_months(sysdate,6)
from dual;

-- 해당일에서 부터 최초로 돌아오는 요일일자
select sysdate, next_day(sysdate,'수요일') from dual;

-- 해당 달의 마지막 날짜를 반환 last_day
select sysdate,last_day(sysdate) from dual;

create table membership(
id varchar2(30) primary key, --not null,unique
name varchar2(30) not null,
pw varchar2(30),
email varchar2(50),
send_email number(1),
zipcode char(5),
address1 varchar2(50),
address2 varchar2(50),
phone char(11),
tel char(11),
birth date,
newyear number(1),
company number(1),
create_date date,
myip char(15)
);

-- primary key 추가
alter table membership add primary key(id);
-- 제약조건 not null 수정
alter table membership modify name not null;

desc membership;

insert into membership values(
'eee','유관순','5555','eee@naver.com',1,'01333','서울 종로구 종로동','101-1',
'01055555555','0255555555','2015/01/01',0,0,sysdate,'101.101.101.27'
);

select * from membership;

commit;

-- 미성년자만 출력하시오.
select birth,months_between(sysdate,birth) from membership
where months_between(sysdate,birth)>216;

create table board(
bno number(4) primary key,
id varchar2(30) not null,
title varchar2(100),
content varchar2(3000),
create_date date,
hit number(4) default 0,
-- 선언 : idex명 mem_fk_id, 외래키(컬럼) 위치 membership테이블 id
constraint mem_fk_id foreign key(id) references membership(id)
);











