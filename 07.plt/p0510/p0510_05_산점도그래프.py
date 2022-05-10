import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# 산점도 그래프

df = pd.read_excel('score.xlsx')
df['학년']=[3,3,2,1,1,3,2,2]
x=df['영어']
y=df['수학']
# 배열구조 랜덤 0<= x < 1 배열구조 8개 생성
# numpy * 1000 = 모든 배열에 * 1000
# sizes = np.random.rand(8)*1000
# sizes = [1000,1000,3000,3000,1000,1000,2000,2000]
sizes = df['학년']*1000


# 산점도 그래프 출력
# s : 원크기설정, c=color, cmap : Colormaps을 사용
plt.scatter(x,y,s=sizes,c=df['학년'],cmap='viridis')
# colorbar : 색상바 출력, ticks:눈금표시, label:색상바 제목출력
# shrink 눈금의 크기 설정, orientation 의 눈금의 위치 horizontal 수평
plt.colorbar(ticks=[1,2,3],label='학년',shrink=0.3,orientation='horizontal')
plt.show()

