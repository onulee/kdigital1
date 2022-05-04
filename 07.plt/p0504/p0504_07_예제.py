import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
# pandas 데이터 정리
# movie.xlsx 영화,관객수 그래프 생성

df = pd.read_excel('movie.xlsx')
# score.xlsx 이름, 합계
x=df['영화']
y=df['평점']

# 선-두께,색상,모양, marker - 크기,테두리색,바탕색,모양
plt.plot(x,y,'bo',markersize=10,label='평점',linestyle='none')
# 범례 위치 - 상단 오른쪽
plt.legend(loc='lower left')
plt.title('흥행영화 관객그래프')
plt.xlabel('영화제목',color='r',loc='center')
plt.ylabel('만명',color='b',loc='center')

plt.show()