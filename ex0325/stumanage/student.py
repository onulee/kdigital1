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
        self.__kor = kor   # private변수선언
        self.eng = eng
        self.total = kor+eng
        self.avg = self.total/2
        
    def setKor(self,kor):
        if kor>=0:
            self.kor=kor
        else:
            print('입력이 잘못되었습니다.')
            # try:
            #     raise Exception('입력이 잘못됨.')
            # except:
            #     pass
                    
    