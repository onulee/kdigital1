--insert ���1
insert into member(id,pw,name,phone) values(
'aaa','1111','ȫ�浿','010-1111-1111');
--insert ���2
insert into member values(
'bbb','1111','�̼���','010-2222-2222');
-- insert ���3 : primary key, �ݵ�� �Է��ؾ� ��.
insert into member(id,pw) values(
'ddd','�豸');

--�˻�
select * from employees;

--����
delete from member where id='bbb';

--����
update member set phone='010-7777-7777' where id='bbb';


select * from departments;

select job_id,job_title,min_salary,max_salary,
create_date,update_date from jobs;

create table member(
id varchar2(20) primary key,
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

desc member;

select * from tab;

select * from member;

insert into member(id,pw,name,phone) values(
'aaa','1111','ȫ�浿','010-1111-1111');

select * from member;

commit;

rollback;

select * from member;

insert into member values(
'eee','1111','������','010-3333-3333');

select * from member;

insert into member values(
'bbb','1111','�̼���','010-2222-2222');

select * from member;
commit;

insert into member values(
'ccc','1111','�̼���','010-2222-2222');

select * from member;

commit;
rollback;


select name,phone from member;

select * from employees;

select emp_name,job_id from employees;

desc employees;

select * from member;

commit;

delete from member;

select * from member;

rollback;

select * from member;

--delete from member where id='bbb';

select employee_id,emp_name,salary from employees where employee_id>=150 and salary>4000;

select * from member;

insert into member values(
'eee','1111','������','010-5555-5555');

commit;

update member set phone='010-7777-7777' where id='bbb';

rollback;

-- students ���̺����
-- stuid,stuname,kor,eng,math,total,avg,rank
-- varchar2(20),number(3),number(4,1)
-- 5���� �л��� �Է��غ�����.


create table students (
stuid varchar2(20),
stuname varchar2(20),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(4,1),
rank number(3)
);

insert into students values(
'5','�豸',99,95,87,99+95+87,(99+95+87)/3,0);

commit;

select * from students;

--drop table member2;

select * from tab;

desc employees;
-- table �÷��߰�
-- alter table member add create_date date;
-- table �÷�����
-- alter table member drop column create_date;
-- ���̺� Ÿ�Ժ���
--alter table member modify pw number(4);
-- ���̺� �÷��̸�����
--alter table member rename column pw to password;
-- ���̺� �̸�����
--alter table member rename to member2; 
-- table���� �� ������ ����
create table member as
select * from member2;
-- table Ÿ�Ը� ����
create table member as
select * from member2 where 1=2;

select * from tab;
commit;
desc member;

update member set pw='';
select * from member;

select * from member;

update member set create_date=sysdate where id='aaa';



alter table member add total number(3);
alter table member add avg number(4,1);

desc member;
select * from member;

desc students;
select * from member;

select * from students;

update students set stuid=6,stuname='������' where kor=99;
commit;

desc students;

desc member;

select * from member;

update member set total=100 where name='ȫ�浿';
update member set total=(select total from students where stuname='ȫ�浿') where name='ȫ�浿';

select * from students;
select total from students where stuname='ȫ�浿';

-- �ߺ��Ǵ� ���� 1���� ���
select distinct manager_id from employees;
select * from employees;

select * from employees;
select emp_name from employees where lower(emp_name)='pat fay';

select * from departments;

-- �̸�, �޿�, �Ի�����
-- emp_name, salary, hire_date, employees;

select emp_name,salary,hire_date from employees where salary>10000;

-- employees�� ���̺��� �Ȱ��� employees2 �����غ�����.

create table employees2 as
select * from employees;

--delete from employees2;

select * from employees2;

--drop table employees2;

select * from employees;

-- employees2 table  create����
-- employee_id, emp_name,hire_date,salary ����

-- 5�� �Է� insert








