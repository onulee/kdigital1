select * from board;

select * from studata;

insert into studata values(
stu_seq.nextval,'홍길연',100,100,92,100+100+92,(100+100+92)/3,1
);

select * from studata
where stuname like '%홍길%';

select * from studata where stuname like '%홍길%';


delete studata where stuname='홍길순';
update studata set kor=90,eng=98,math=90,total=(90+98+90),avg=(90+98+90)/3 where stuname='홍길동';


commit;
rollback;

select * from studata;

select count(*) from studata;