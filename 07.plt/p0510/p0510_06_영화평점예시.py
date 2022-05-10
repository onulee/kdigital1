# 대한민국 영화 중에서 관객 수가 가장 많은 상위 8개의 데이터  
# 1. 개봉연도별 선그래프를 출력하시오.
# - 선은 red, marker o, 선은 직선
# - x축 눈금표시 2005,2010,2015,2020
# - Y축 눈금범위 7,10 

import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np
data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2016, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data).sort_values('개봉 연도')
# sort_values index를 reset해줘야 설정이 됨.
df = df.reset_index(drop=True)
print(df)
# print(df.index)
# x = list(df['개봉 연도'])
# y = list(df['평점'])
x = df['개봉 연도']
y = df['평점']

plt.plot(x,y,'ro--')
# x그래프 눈금 2005,2010,2015,2020
plt.xticks([2005,2010,2015,2020])
plt.ylim(7,10)
plt.title('개봉연도별 관객수 그래프')
for i,txt in enumerate(y): # i : 0,1,2,3,4,5,6,7
    if i%2==0:
        plt.text(x[i],y[i]+0.1,txt,ha='center')
    else:
        plt.text(x[i],y[i]-0.2,txt,ha='center')
            
            
plt.show()

