# score 5명의 학생의 국어성적을 원그래프로 출력하시오.
# 테두리 흰색, 도넛형태 꾸미기
# 10이하는 생략 글자 넣기

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

df = pd.read_excel('score.xlsx')
# 5개데이터 가져오기, 국어 기준으로 역순정렬
# df_2 = df.head(5).sort_values('국어',ascending=False)
df_2 = df[:5].sort_values('국어',ascending=False)

# 원그래프
values = df_2['국어']
labels =df_2['이름']
colors =['#ffebb5','#ffc0b5','#dbffb5','#b5f9ff','#b5b9ff']
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}
def auto_pct(pct):
    return '{:.1f}%'.format(pct) if pct>10 else ''
plt.figure(figsize=(8,5))
explode = [0,0,0,0,0]
plt.pie(values,labels=labels,colors=colors, \
    wedgeprops=wedgeprops,explode=explode,autopct=auto_pct,\
        pctdistance=0.7,startangle=90,counterclock=False)
plt.title('국어성적 그래프')
# 범례넣기
plt.legend(loc=(1.1,0.3))
plt.show()