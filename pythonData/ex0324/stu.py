class Student:
    stuNo=0
    stuName=''
    stuKor=0
    stuEng=0
    stuTotal=0
    stuAvg=0
    stuRank=0
    
    # 클래스 생성시 최초 1회 실행
    def __init__(self,stuName,stuKor,stuEng):
        # 클래스변수에서 1증가해서 자동입력
        Student.stuNo += 1
        self.stuNo = Student.stuNo
        self.stuName = stuName
        self.stuKor = stuKor
        self.stuEng = stuEng
        self.stuTotal = stuKor+stuEng
        self.stuAvg = (stuKor+stuEng)/2
    
    # 객체를 호출시 자동으로 함수 실행.    
    def __str__(self):
        return '{},{},{},{}'.format(self.stuNo,self.stuName,\
            self.stuKor,self.stuTotal )
    
    def setStukor(self,stuKor):
        if stuKor>=0:
            self.stuKor = stuKor
            self.stuTotal = stuKor + self.stuEng
            self.stuAvg = self.stuTotal/2
        else:
            print('입력값이 잘못되었습니다.')  
    
    
    # 실행하는 곳이 자신인지 확인    
    if __name__ == '__main__':
        print('현재 자신에서 호출되어 실행함. 클래스 이름은 '+'Student') 
        # print(stuNo) 
    else:
        print('Student클래스가 호출 됨')      