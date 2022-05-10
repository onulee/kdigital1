# 지역별 인구현황 막대 그래프 출력하시오.
# 지역별 인구현황을 원그래프 만들어보세요.

import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# 1. 데이터 가져오기 : 연령별 인구현황.xlsx
# skiprows : 상단부분3개 제외, nrows : 1개줄만 가져옴, usecols-> 컬럼을 가져오는 것.
# 1) 전국 남자 컬럼 인구현황만 가져옴.
df_m = pd.read_excel('201201_인구현황.xlsx',skiprows=3,nrows=1,index_col='행정기관',usecols='B,E:Y')
# df.iloc[0] 0번째 index줄을 ,를 삭제 후, int타입으로 형변환
df_m.iloc[0] = df_m.iloc[0].str.replace(',','').astype(int)

# 2) 전국 여자 컬럼 인구현황만 가져옴.
df_w = pd.read_excel('201201_인구현황.xlsx',skiprows=3,nrows=1,index_col='행정기관',usecols='B,AB:AV')
df_w.iloc[0] = df_w.iloc[0].str.replace(',','').astype(int)
df_w.columns = df_m.columns


# 막대 그래프
# x,y축 데이터 대입
y = df_m.columns
x1 = df_m.iloc[0]//1000
x2 = df_w.iloc[0]//1000

plt.barh(y,x1,label='남자')
plt.barh(y,-x2,label='여자')
plt.xlabel('단위:천명',loc='right')
plt.title('2012년도 연령별 인구현황 그래프')
plt.legend()
plt.show()


print(df_w)


