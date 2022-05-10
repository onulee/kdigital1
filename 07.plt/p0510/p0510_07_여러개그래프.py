import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# 여러개 그래프 
# 1개 그래프 - plot,bar,barh,pie,scatter
# x=[1,2,3]
# y=[2,4,8]

# plt.plot(x,y)
# plt.show()

df = pd.read_excel('score.xlsx')
# plt.plot(x,y) - 1개 그래프
# 2행2열의 그래프 생성
fig,axs = plt.subplots(2,2,figsize=(15,8))
# suptitle : 전체제목  
fig.suptitle('4개의 전체제목 그래프')
# 1행1열부분 그래프 생성
x = df['이름']
y = df['국어']
z = df['영어']
z2 = df['수학']
# label:범례제목
axs[0,0].bar(x,y,label='국어')
# set_title : 1개의 그래프 위 제목
axs[0,0].set_title('국어막대그래프')
# xlabel,ylabel : 눈금제목
axs[0,0].set(xlabel='이름',ylabel='국어점수')
# set_facecolor : 배경색
axs[0,0].set_facecolor('#fff2cf')
axs[0,0].grid(linestyle='--',linewidth=0.5)
axs[0,0].legend()
# label : 범례
axs[0,1].plot(x,z,label='영어')
axs[0,1].plot(x,z2,label='수학')
axs[0,1].legend(loc='lower right')
axs[1,0].barh(x,df['키'])
axs[1,1].plot(x,df['사회'],color='g',alpha=0.5)


plt.show()