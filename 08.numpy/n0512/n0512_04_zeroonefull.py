import numpy as np

list_data = [1,2,3,4,5]
np.array(list_data) #list타입 변경
np.arange(1,10)     # arange
np.linspace(1,10,3) #linspace

# numpy행렬 값 : 0으로 세팅
# arr = np.zeros(4)   #zeros

# zeros : 2차원행렬을 0으로 세팅
# arr = np.zeros((3,3))
# arr = np.zeros((4,3))
# arr = np.zeros((2,2),dtype=float)

# ones : 1로 세팅 : dtype-타입을 변경 - str,float,int
# arr = np.ones((2,2),dtype=str)

# full : 원하는 값으로 세팅
# arr = np.full(10,5)  # 1차원 행렬 10개 : 5
# arr = np.full((3,3),7) # 2차원(2x2) 행렬 : 7

# 단위행렬 : 대각선 : 1, 나머지 0
arr = np.eye(4)

print(arr)