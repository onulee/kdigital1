# 막대 그래프
import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd

# 국어,영어,수학 누적막대그래프
df = pd.read_excel('score.xlsx')
x = df['이름']
# x = [0,1,2,3,4,5,6,7]
y1 = df['국어']
y2 = df['영어']
y3 = df['수학']
plt.figure(figsize=(8,5))

# 가로누적막대그래프 - bottom 점수를 추가해서 그래프를 그려줌.
plt.barh(x,y1)
plt.barh(x,y2,left=y1)
plt.barh(x,y3,left=y1+y2)
# plt.yticks(x,df['이름'])
plt.show()

# 세로누적막대그래프
# plt.bar(x,y1,label='국어')
# plt.bar(x,y2,bottom=df['국어'], label='영어')
# plt.bar(x,y3,bottom=df['국어']+df['영어'],label='수학')
# plt.grid(alpha=0.5,axis='y')
# # 범례 가로로 3개 표시
# plt.legend(ncol=3)
# # plt.yticks([0,160,170,180,190,200,210])
# plt.ylim(0,8)
# plt.show()