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
       
    def setKor(self,kor):
        if kor>=0:
            self.kor = kor
            self.total = kor + self.eng
            self.avg = self.total/2
        else:
            print('입력값이 잘못되었습니다.')  
            
    def getKor(self):
        return self.kor          