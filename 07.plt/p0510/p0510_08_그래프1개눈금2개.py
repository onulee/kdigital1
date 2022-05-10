import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np
df = pd.read_excel('score.xlsx')

x=df['이름']
y=df['키']
# y=[1100,1200,1500,1600,1000,1300,1100,1400]
z=df['국어']

# 여러개 그래프
# 1번째 그래프
fig,ax1 = plt.subplots()
ax1.set_ylabel('키')
ax1.set_ylim(160,210)
for i,val in enumerate(y):
    if (i==0) | (i==2) :
        ax1.text(i,val-4,val,ha='center')
    else:
        ax1.text(i,val+2,val,ha='center')
ax1.plot(x,y,'o-')

# 2번째.ax1과 x축은 동일한 것을 사용
ax2 = ax1.twinx()
ax2.set_ylabel('국어')
ax2.set_ylim(10,110)
ax2.plot(x,z,'x--')
for i,val in enumerate(z):
    ax2.text(i,val+2,val,ha='center')


# 1개그래프일때
# plt.plot(x,y)
# plt.plot(x,z)

plt.show()