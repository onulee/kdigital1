class Graphic2d:
    x=0
    # 그래픽을 보여주기....100만줄
    # 수정 10만줄
    
    def gprint(self):
        return '{}'.format(self.x)
       
        
class Graphic3d(Graphic2d):
    z=0
    
    def gprint(self):    # 오버라이딩
        # return '{},{},{}'.format(self.x,self.y,self.z)
        return '{},{}'.format(super().gprint(),self.z)
        

g1 = Graphic2d()
print(g1.gprint())

g2 = Graphic3d()
print(g2.gprint()              )