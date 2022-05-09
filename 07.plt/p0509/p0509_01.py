import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd

df = pd.read_excel('score.xlsx')

x=df['지원번호']
y=df['키']
# x=[1,2,3]
# y=[-2,-4,8]

# r-color, o-marker,-- - linestyle
plt.plot(x,y,'ro--',label='키')
plt.title('학생 그래프',color='r')
plt.xlabel('학생번호',color='red')
plt.ylabel('키',color='g')
# plt.xticks([1,2,3,4,5,6,7,8])
# plt.yticks([0,100,200])
plt.grid(axis='x')

plt.legend()
plt.show()
