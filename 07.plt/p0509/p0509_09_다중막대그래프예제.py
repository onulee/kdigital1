# stu1000
# 합계점수가 높은, 1학년 5명을 
# 국어,영어,수학,과학 그래프 출력하시오.
import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# 1. 합계컬럼 생성
df = pd.read_excel('stu1000.xlsx')
df['합계'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']


# 2. 1학년이면서 점수가 높은 순으로 정렬
#  1차 학년에 먼저 순차정렬, 2차 합계는 역순정렬
# 합계점수 역순정렬 , 학년 순차정렬 sort
print(df.sort_values(['학년','합계'],ascending=[True,False]))
find_df = df.sort_values(['학년','합계'],ascending=[True,False]).head()


# 3. 각 컬럼 데이터 생성
names=find_df['이름']

y1=find_df['국어']
y2=find_df['영어']
y3=find_df['수학']
y4=find_df['과학']


# 4. 다중막대그래프 그리기
x = np.arange(5)
plt.figure(figsize=(8,5))
plt.bar(x-0.3,y1,label='국어',width=0.2)
plt.bar(x-0.1,y2,label='영어',width=0.2)
plt.bar(x+0.1,y3,label='수학',width=0.2)
plt.bar(x+0.3,y4,label='과학',width=0.2)
# xticks for문 위에 둠.
plt.xticks(x,find_df['이름'])


# 5. 막대그래프 데이터값 출력
# for x,y1,y2,y3,y4 in zip(x,y1,y2,y3,y4):
#     plt.text(x-0.3,y1+1,y1,ha='center')
#     plt.text(x-0.1,y2+1,y2,ha='center')
#     plt.text(x+0.1,y3+1,y3,ha='center')
#     plt.text(x+0.3,y4+1,y4,ha='center')

# for문을 y1,y2,y3,y4 4번을 실행해도 됨.    
for i,txt in enumerate(y1):
    plt.text(i-0.3,txt+1,txt,ha='center')
for i,txt in enumerate(y2):
    plt.text(i-0.1,txt+1,txt,ha='center')
for i,txt in enumerate(y3):
    plt.text(i+0.1,txt+1,txt,ha='center')
for i,txt in enumerate(y4):
    plt.text(i+0.3,txt+1,txt,ha='center')

# 눈금표시 30부터 110으로 변경
plt.ylim(50,120)
plt.legend(ncol=4,loc='upper center')
plt.show()
