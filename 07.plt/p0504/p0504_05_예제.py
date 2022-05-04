import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.size']=15

df = pd.read_excel('score.xlsx')
# score.xlsx 이름, 합계
df['합계'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
x=df['이름']
y=df['합계']

# 범례 - 성적
# title - 학생성적그래프
# x - 이름
# y - 점수
plt.plot(x,y,label='성적')
# 범례 위치 - 상단 오른쪽
plt.legend(loc='upper right')
plt.title('학생성적그래프')
plt.xlabel('이름',color='r',loc='center')
plt.ylabel('점수',color='b',loc='center')

plt.show()
