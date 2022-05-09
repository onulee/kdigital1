# 막대 그래프
import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# 다중막대그래프
df = pd.read_excel('score.xlsx')

# x=df['이름']
# x=[0,1,2,3,4,5,6,7]
y1=df['국어']
y2=df['영어']
y3=df['수학']

# 막대그래프에 데이터값을 표시
# 강나래-2
# plt.text(0,90+2,100,ha='center')
# plt.text(1,40,40,ha='center')
# for i,txt in enumerate(y1):
#     plt.text(i,y1[i]+2,txt,ha='center')
# x=[0,1,2,3,4,5,6,7]-0.25 = ?
# 함수를 만들어서 실행



### x list만들기
# # x = [0,1,2,3,4,5,6,7]
# x=[]
# for i in range(8):
#     x.append(i)
# # print(x)

# # 0.25를 전체적으로 빼기해서, y list을 만들기
# y=[]
# for i in x:
#     y.append(i-0.25)
# print(y)  

# numpy를 생성후 -0.25 계산실행
# x = [0 1 2 3 4 5 6 7]
x = np.arange(8)
plt.figure(figsize=(8,5))
plt.bar(x-0.25,y1,label='국어',width=0.25)
plt.bar(x,y2,label='영어',width=0.25)
plt.bar(x+0.25,y3,label='수학',width=0.25)

# 눈금표시 30부터 110으로 변경
plt.ylim(0,110)
plt.xticks(x,df['이름'])
print(type(df['이름']))
# plt.legend()
# plt.show()