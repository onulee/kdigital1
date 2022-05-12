import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np


# random
# numpy행렬, 일률적으로 숫자를 입력해서 행렬
# randint 랜덤으로 0부터 9까지 숫자를 랜덤으로 생성, 3행3열 행렬생성
# arr = np.random.randint(0,10,(3,3)) #2차원행렬
# arr = np.random.randint(30,50,5)       #1차원행렬

# 0부터 1이전까지 실수타입 8개 행렬
# arr = np.random.rand(8)*100  

# normal 평균이 0이고, 표준편차가 1인 표준정규분포 배열
arr = np.random.normal(0,1,(3,3))
    
print(arr)

# x=[1,2,3,4,5]

# plt.plot(x,arr)
# plt.ylim(10,50)
# plt.show()