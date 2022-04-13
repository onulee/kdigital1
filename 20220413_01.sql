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













