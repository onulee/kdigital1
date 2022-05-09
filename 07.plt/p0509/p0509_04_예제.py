# df[키] -> 키 그래프를 그리고, 키높이를 표시하시오.

import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd

df = pd.read_excel('score.xlsx')
x = df['지원번호']
y = df['키']
# ro-- : r-색상, o-marker, -- - linestyle
plt.plot(x,y,'o-', label='키')
plt.title('학생 그래프')



for i,txt in enumerate(y):
    if i==2:
        plt.text(x[2],y[2]-4,txt,ha='center')
        continue
    plt.text(x[i],y[i]+2,txt,ha='center')
plt.yticks([160,170,180,190,200,210])
plt.show()