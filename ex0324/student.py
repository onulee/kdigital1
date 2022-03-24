
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
       self.avg = (kor+eng)/2
       
    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,self.stuname,\
            self.kor,self.eng,self.total,self.avg,self.rank)    
    
    def setStuname(self,stuname): #홍길동aaa1
        tempno=0
        for name in stuname:
            if not name.isdigit():
                print('문자만 입력이 가능합니다.')
                tempno=1
                break
        if tempno==0:    
            self.stuname = stuname       
    
       
    def setKor(self,kor):
        if kor>=0:
            self.kor = kor
            self.total = kor + self.eng
            self.avg = self.total/2
        else:
            print('입력값이 잘못되었습니다.')  
            
    def getKor(self):
        return self.kor          