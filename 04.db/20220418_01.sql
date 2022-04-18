select * from board order by bno desc;

insert into board values(
board_seq.nextval,'aaa','[답글]게시판제목2','게시판2의 답글입니다.',sysdate,1
);


desc member;
commit;

create table tboard (
bno number(4) primary key,
id varchar2(20) not null,
btitle varchar2(200) not null,
bcontent varchar2(3000),
bdate date default sysdate,
bgroup number(4) not null,
bstep number(4),
bindent number(4),
bhit number(4),
bimg varchar2(200),
constraint membership_fk_id foreign key(id) references membership(id)
);

desc tboard;

select * from tboard;
insert into tboard values(
b_seq.nextval,  --bno
'aaa',          --id
'[답글][답글] 5번째 게시글',  -- btitle
'[답글답글입니다.] 5번', --bcontent
sysdate,             -- bdate
5,       -- bgroup
2, --bstep
2, --bindent
1, --bhit
'1.jpg' --bimg
);

commit;

select * from tboard order by bgroup desc,bstep asc;

select employee_id,emp_name,manager_id from employees;

select employee_id,emp_name,manager_id from employees
where manager_id is null;

-- self join, out join
select e1.employee_id,e1.emp_name,e1.manager_id,e2.emp_name
from employees e1,employees e2
where e1.manager_id = e2.employee_id(+)
order by e1.employee_id
;

select employee_id,emp_name,department_id from employees;


-- equi join 
-- employees,departments테이블을 equi join을 해서
-- 사원번호,사원이름,부서번호,부서이름을 출력하시오.
-- employee_id,emp_name,department_id,department_name

-- inner join equi join
select employee_id,emp_name,employees.department_id,department_name
from employees,departments
where employees.department_id = departments.department_id(+)
order by employee_id;

-- equi join
select emp_name,department_name from employees e,departments d
where e.department_id = d.department_id;

-- ansi inner join
select emp_name,department_name from employees e inner join departments d
on e.department_id = d.department_id;

-- ansi using
select e.emp_name, d.department_name from employees e inner join departments d
using (department_id);

-- natural join employees,departments 공통컬럼을 찾아서 조인을 자동으로 시켜줌.
select e.emp_name,d.department_name 
from employees e natural join departments d;

-- out join
select employee_id,emp_name,e.department_id, department_name 
from employees e, departments d
where e.department_id = d.department_id(+); 
-- employees테이블의 department_id가 null이더라도 출력을 해주세요.

-- ansi join out join
select employee_id,emp_name,department_id,department_name
from employees e full outer join departments d
using(department_id);








