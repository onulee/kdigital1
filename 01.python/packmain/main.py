import sys
# 동등한 폴더에 위치했을때
sys.path.append('.')
# sys.path.append('/pydata')
# sys.path.append('C:/pydata')
# from packsub.stu1 import Stu_seoul
# import packsub.stu1 

# 하부폴더에 위치했을때
# from packsub2.stu1 import Stu_seoul
print(sys.path)
s1 = Stu_seoul()
# s1 = packsub.stu1.Stu_seoul()
s1.schoolseoul()