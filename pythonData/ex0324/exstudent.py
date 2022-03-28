from unicodedata import name


class Student:
    stuno=0
    stuname=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    def __init__(self,stuno,stuname,kor,eng):
       self.stuno = stuno 
       self.stuname = stuname
       self.kor = kor
       self.eng = eng
       self.total = kor+eng
       self.avg = self.total/2