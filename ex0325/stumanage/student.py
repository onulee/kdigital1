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
        # self.__kor = kor   # private변수선언-같은클래스 내에서만 입력가능
        self.kor = kor   
        self.eng = eng
        self.total = kor+eng
        self.avg = self.total/2
        
    def __eq__(self,other):
        return self.stuname == other.stuname and \
            self.stuno == other.stuno   
    
    def getKor(self):
        return self.__kor
        
    def setKor(self,kor):
        if kor>=0:
            self.__kor=kor
        else:
            print('입력이 잘못되었습니다.')
            # try:
            #     raise Exception('입력이 잘못됨.')
            # except:
            #     pass
                    
    