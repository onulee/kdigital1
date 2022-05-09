# 막대 그래프
import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd

df = pd.read_excel('score.xlsx')

label=df['이름']
values=df['키']

# 막대그래프 - 가로버전 : barh를 하면 가로버전출력
# plt.barh(label,values)

# bar 패턴 그리기 : set_hatch
# figure 이미지 확대
plt.figure(figsize=(8,5))
bar = plt.bar(label,values)
bar[0].set_hatch('//')
bar[1].set_hatch('x')
bar[2].set_hatch('..')
# plt.barh(label,-values2)

# 그래프 데이터 값넣기
for i,txt in enumerate(values):
    # 막대그래프 x:0,1,2,3,4,5,6,7  values:[키]
    plt.text(i,values[i]+1.5,txt,ha='center')

plt.ylim(165,210)
plt.show()
