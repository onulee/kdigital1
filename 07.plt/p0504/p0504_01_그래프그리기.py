import pandas as pd
import matplotlib.pyplot as plt

# pandas 데이터 불러오기
df = pd.read_excel('./score.xlsx')
print(df['지원번호'])
print(df['국어'])

# 데이터 정보 ( x, y )
# x=[1,2,3]
# y=[2,4,8]
x=df['지원번호']
y=df['국어']
z=df['수학']

# plot : 그래프 생성
# plt.plot(x,y)   : 선 그래프 생성
plt.plot(x,y)    # : 바 그래프 생성
plt.plot(x,z)   # 선을 2개 그리려면 x,y x,z선이 2개가 그려짐.
# 그래프 보여줌
plt.show()