# stu1000 -> 학년별 비율을 원그래프로 출력하시오.
# 1학년 
# 2학년
# 3학년

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

df = pd.read_excel('stu1000.xlsx')
print(df)
# df_2 = df.groupby('학년').size()[1]  # 1학년 인원 int타입
df_2 = df.groupby('학년').size()       # Series
# print(df_2[0])
# Series 1차원배열 : pandas타입
df_2 = list(df_2)  # Series -> list타입변경가능
# print(df_3[0])

# for i, (rank,cnt) in enumerate(df_2.iteritems()):
#     print(i,rank,cnt)

# print(df_2)

# 원그래프
# list타입의 1,2,3학년 데이터 값
values = df_2
labels =['1학년','2학년','3학년']
colors =['#ffebb5','#ffc0b5','#dbffb5']
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}

plt.figure(figsize=(8,5))
explode = [0,0,0]
plt.pie(values,labels=labels,colors=colors, \
    wedgeprops=wedgeprops,explode=explode,autopct='%.1f%%',\
        pctdistance=0.7,startangle=90,counterclock=False)
plt.title('학년별 인원 그래프')
# 범례넣기 - title을 하면 범례에 제목입력
plt.legend(loc=(1.1,0.3),title='학년별 인원')
plt.show()




   
