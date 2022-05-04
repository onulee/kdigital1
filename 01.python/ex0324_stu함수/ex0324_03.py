# Car 
# color,tire,speed
# upSpeed -> 입력받은 속도만큼 speed증가
# downSpeed -> 입력받은 속도만큼 speed감소

class Car:
    color=''
    tire=0
    speed=0
    
    def upSpeed(self,speed):
        self.speed += speed
        
    def downSpeed(self,speed):
        self.speed -= speed
 
            
c1 = Car()
c1.color='red'
c1.tire = 5
c1.upSpeed(100)
c1.downSpeed(30)
print('{},{},{}'.format(c1.color,c1.tire,c1.speed))

 
# c1 객체선언후
# 색상:red, 타이어 5개,속도 100증가, 속도 30감소

# 색상,타이어,speed를 출력하시오.