# 막대 그래프
import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd

# 다중막대그래프
df = pd.read_excel('score.xlsx')

# x =['강나래','강태원',2,3,4,5,6,7]
# x=df['이름']
x=[0,1,2,3,4,5,6,7]
y1=df['국어']
y2=df['영어']
y3=df['수학']

plt.bar(0,90,label='국어',width=0.1)
plt.bar(1,100,label='국어',width=0.1)
plt.bar(2,80,label='국어',width=0.1)
plt.bar(3,70,label='국어',width=0.1)
plt.bar(4,100,label='국어',width=0.1)
plt.bar(5,90,label='국어',width=0.1)
plt.bar(6,60,label='국어',width=0.1)
plt.bar(7,90,label='국어',width=0.1)
# plt.bar(x,y1,label='국어',width=0.3)
# plt.bar(x,y2,label='영어',width=0.3)
plt.legend()
plt.show()