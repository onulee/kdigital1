import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# 원그래프
values = [30,25,20,13,10,2]
labels =['python','java','javascript','c#','c++','etc']

colors =['#ffebb5','#ffc0b5','#dbffb5','#b5f9ff','#b5b9ff','#fbb5ff']
plt.figure(figsize=(8,5))
# 거리 띄우기
explode = [0,0,0,0,0,0]

# 글자를 나타날때 10이하는 생략하는 함수
def custom_autopct(pct):
    if pct > 10:
       return '{:.1f}%'.format(pct) # return '30.0%'
    else:
       return ''                    # return ''

# edgecolor:테두리 색상, linewidth: 테두리 두께, width: 도넛형태 0~1까지 거리
wedgeprops = {'edgecolor':'w','linewidth':2,'width':0.6}
# pie 데이터는 list형태 : 순차적으로 실행
# pctdistance : 글자 거리, 1에 가까울수록 원테두리에 근접
plt.pie(values,labels=labels,colors=colors, explode=explode,\
    wedgeprops=wedgeprops,autopct=custom_autopct,startangle=90,\
        counterclock=False,pctdistance=0.7)
plt.title('원그래프')
# 범례넣기
plt.legend(loc=(1.1,0.3))
plt.show()