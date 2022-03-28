class Student:
    stuno=0
    name=''
    kor=0
    eng=0
    total=0
    avg=0
    rank=0
    
    # 생성자
    def __init__(self,stuno,name,kor,eng):
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.total = kor+eng
        self.avg = (kor+eng)/2
    
s1 = Student(1,'홍길동',100,100)  
s2 = Student(2,'이순신',90,90)  
s3 = Student(3,'유관순',100,99)  
s4 = Student(4,'강감찬',90,95)  

stuList = [s1,
           s2,
           s3,
           s4]
 

print(stuList[0].name)

    



# class Student:
#     stuno=0
#     name=''
#     kor=0
#     eng=0
    
# # 시작
# s1 = Student()
# s1.stuno=1
# s1.name='홍길동'
# s1.kor=100
# s1.eng=100

# s2 = Student()
# s2.stuno=2
# s2.name='이순신'
# s2.kor=90
# s2.eng=90

# s3 = Student()
# s3.stuno=3
# s3.name='유관순'
# s3.kor=100
# s3.eng=99


# print(s1.name)
    