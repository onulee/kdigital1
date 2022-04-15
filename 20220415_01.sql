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


-- 조건을 사용한 decode함수 이용해서 결과출력, CLERK, MAN, REP, ACCOUNT
select employee_id,emp_name,job_id,salary,
decode(substr(job_id,4),
'CLERK',salary*0.05,
'MAN',salary*0.07,
'REP',salary*0.04,
'ACCOUNT',salary*0.06
) as "월급인상현황" from employees;

-- 조건 case함수 사용
select employee_id,emp_name,job_id,salary,
case 
when substr(job_id,4)='CLERK' then salary*0.05
when substr(job_id,4)='MAN' then salary*0.07
when substr(job_id,4)='REP' then salary*0.04
when substr(job_id,4)='ACCOUNT' then salary*0.06
else salary
end
as "월급인상현황" from employees;

-- studata avg 90점 이상 A, 80점이상 B, 70점이상 C, 60점이상 D "성적결과"
select * from studata;

select stuno,stuname,avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
end
as "성적처리결과"
from studata;

select count(*),count(manager_id),count(commission_pct) from employees;

select count(*)-count(commission_pct) as "노커미션",count(commission_pct) "커미션" from employees;

select count(*) from employees
where commission_pct is null;


select department_id,count(*),to_char(avg(salary),999999.99), sum(salary) from employees
group by department_id
;

select emp_name,salary from employees;

select department_id,department_name from departments;
select department_id,salary from employees where department_id=60;

select department_id,max(salary),min(salary) from employees
where department_id=60
group by department_id;

-- 50번 부서의 최대로 월급을 많이 받는 사람의 
-- 사번,이름,부서,월급을 출력하시오.

select employee_id,emp_name,department_id,salary from employees
where salary=(
select max(salary) from employees
where department_id=60
) and department_id=60;

-- 부서별, 전체인원수, 커미션을 받는사람수, 받지 않는 사람수 출력하시오.
select department_id,count(*),count(commission_pct),count(*)-count(commission_pct)
from employees
group by department_id;

select department_id,avg(salary) from employees
where department_id>40
group by department_id
having avg(salary)>=4000
order by department_id
;

-- 부서별 최대월급을 출력을 하는데, 5000달러 이상인 최대값만 출력하시오.
select department_id,max(salary) maxsalary from employees
group by department_id
having max(salary)>5000
order by maxsalary;

select department_id,department_name from employees;
select department_id,department_name from departments;

create table employees2 as
select department_id,department_name from departments;

update employees2 set department_name='기획부'
where department_id=10;

select * from employees2; --컬럼2
select * from departments; --컬럼6

select * from employees2,departments;

-- equi join : 동일한 컬럼을 가지고 검색
select employee_id,emp_name,e.department_id,department_name,
salary,job_id
from employees e,departments d
where e.department_id = d.department_id;

--equi join employees,jobs테이블
--employee_id,emp_name,job_id, job_title 넣어서 출력하시오.
select employee_id,emp_name,e.job_id,job_title
from employees e,jobs j
where e.job_id = j.job_id;

select * from board;
-- bno,name,title,content,create_date,hit
-- membership,board 조인해서 출력을 하시오.
select * from membership;


select bno,name,title,content,b.create_date,hit
from membership m,board b
where m.id=b.id;


-- 테이블 : employees,jobs,departments 3개 조인
-- 컬럼 : employee_id,job_id,job_title,department_id,department_name
-- 조건 : employee_id >150 이상이면서, 이름이 s,S가 들어가 있는 사람만 출력하시오.
select employee_id,emp_name,e.job_id,job_title,e.department_id,department_name
from employees e,jobs j,departments d
where e.job_id = j.job_id and e.department_id=d.department_id and employee_id>150 
and lower(emp_name) like '%s%'
order by employee_id;

select employee_id,emp_name,e.job_id,job_title,e.department_id,department_name
from employees e,jobs j,departments d
where e.job_id = j.job_id and e.department_id=d.department_id(+)
order by employee_id;

select * from employees order by employee_id;

select * from employees
where department_id is null;

select * from departments;

select * from countries;

select * from kor_loan_status;

SELECT period, region, SUM(loan_jan_amt) totl_jan
FROM kor_loan_status
WHERE period = '201311'
GROUP BY period, region
HAVING SUM(loan_jan_amt) > 100000
ORDER BY region;




select * from kor_loan_status;

-- group by 그룹함수 sum 사용
-- region 지역별 대출총액을 출력하시오.
select region,sum(loan_jan_amt) from kor_loan_status
group by region;

-- 4자리 년도만 가지고 년도별,지역별 대출총액을 출력하시오.
select substr(period,0,4) new_period,region,sum(loan_jan_amt) from kor_loan_status
group by substr(period,0,4),region
order by sum(loan_jan_amt) desc,new_period;



create table salary_grade(
grade number(1),
low_salary number(5),
high_salary number(5)
);
select salary from employees order by salary;
insert into salary_grade values(
5,10001,30000
);

commit;

-- non-equi 조인 : 상관관계가 없는 두 테이블 서로 조인
select * from salary_grade;
select * from employees;

select employee_id,emp_name,salary,grade
from employees,salary_grade
where salary between low_salary and high_salary
order by employee_id
;

select employee_id, emp_name,salary,
case when salary>=10001 then 5
when salary>=8001 then 4
when salary>=5001 then 3
when salary>=3001 then 2
when salary>=2000 then 1
end as grade
from employees
order by employee_id
;
select * from studata;
-- non-equi조인 사용
-- studata,stu_grade테이블에서 stuno,stuname,grade 컬럼을 출력하시오.
-- stu_grade 테이블 생성 : grade char(2),low_score number(3),high_score number(3) 
-- 100-95 A+, 94-90 A, 89-85 B+, 84-80 B, 79-0 C 

select stuno,stuname,avg,grade
from studata,stu_grade
where avg between low_score and high_score
order by stuno
;

create table stu_grade(
grade char(2),
low_score number(3),
high_score number(3)
);

insert into stu_grade values(
'C',0,79
);

commit;

select * from stu_grade;

-- self join : 자신 테이블 2개를 가지고 조인하는 것
--     e1: 컬럼항목을 출력, e2는 또다른 검색해서 출력
select e1.employee_id,e1.emp_name,e1.manager_id,e2.emp_name 
from employees e1, employees e2
where e1.manager_id=e2.employee_id  -- manager_id와 employee_id와 비교
order by e1.employee_id
;

select employee_id,emp_name,manager_id
from employees 
;

select employee_id,department_id from employees;
select department_id,department_name from departments;

--equi조인
select employee_id,emp_name,employees.department_id,department_name
from employees,departments
where employees.department_id=departments.department_id

select employee_id,emp_name,manager_id from employees;
select employee_id,emp_name from employees where employee_id=124;

--self 조인
select e1.employee_id,e1.emp_name,e1.manager_id,e2.emp_name
from employees e1,employees e2
where e1.manager_id=e2.employee_id;

--outjoin 조인 +추가
select e1.employee_id,e1.emp_name,e1.manager_id,e2.emp_name
from employees e1,employees e2
where e1.manager_id=e2.employee_id(+);










