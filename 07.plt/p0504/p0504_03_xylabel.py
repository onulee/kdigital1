import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # title 한글표시
matplotlib.rcParams['axes.unicode_minus'] = False    # title -표시
matplotlib.rcParams['font.size'] = 15

df = pd.read_excel('score.xlsx')
x=df['이름']
y=df['국어']
plt.plot(x,y) # 그래프 생성
# 상단title
plt.title('실적그래프')
# 그래프 x,y표시설명
plt.xlabel('이름',color='#0000ff',loc='right')     # loc = left,center,right
plt.ylabel('국어점수',color='#00ff00',loc='top')   # loc = top,center,bottom

# 그래프 보여줌.
plt.show()