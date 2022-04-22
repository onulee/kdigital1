# 클래스의 이름 대문자, 변수 소문자, 함수 소문자()
class Car:  
    color="white"
    speed=0
    
    def upSpeed(self,speed):
        self.speed += speed
        
    def downSpeed(self,speed):
        self.speed -= speed
        
a = Car() 
a.upSpeed(10)
print(a.speed)      



    
    