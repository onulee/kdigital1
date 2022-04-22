--drop table studata2;
select stuno,stuname,total,rank() over(order by total desc) as ranks
from studata2 order by stuno;

update studata a set rank=
(
select ranks from 
(select stuno,rank() over(order by total desc) as ranks from studata) b
where a.stuno=b.stuno
);

update studata set rank=1;

commit;

select * from studata;

select a.employee_id,a.emp_name,a.manager_id,b.emp_name
from employees a, employees b
where a.manager_id=b.employee_id(+);


select employee_id,b.department_id,department_name
from employees a,departments b
where a.department_id=b.department_id;


select stuno,rank() over(order by total desc) as ranks from studata2;

select * from studata2 b;

select rank() over(order by total desc) as ranks from studata2;

select stuno,stuname,total,rank from studata2;




create table studata2 as
select * from studata;



update studata2 set rank=1;
commit;



update studata a
set rank=(select ranks from 
(select stuno, rank() over(order by total desc) as ranks from studata) b 
where b.stuno = a.stuno);


