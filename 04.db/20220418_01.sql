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








