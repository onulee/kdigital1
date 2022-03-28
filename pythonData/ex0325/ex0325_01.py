class Car:
    color='white'
    tire=4
    speed=0
    def upSpeed(self,speed):
        self.speed=speed
        print('현재속도 :',self.speed)
        
 
class Sedan(Car):
    pass 
 
class Truck(Car):
    pass
 

c1 = Sedan()
print(c1.speed) 
       