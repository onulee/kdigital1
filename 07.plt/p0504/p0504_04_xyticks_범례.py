import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

x=[1,2,3]
y=[192,194,198]

# 그래프 선의 범례설정 - label입력후 legend함수 호출해야 함.
plt.plot(x,y, label='키높이')
# plt.legend(loc=(0.1,0.8))
plt.legend(loc=('upper left')) #upper,lower,left,right
plt.title('키높이 그래프')
# x,y 그래프 주석표시
plt.xlabel('번호',color='blue',loc='center')
plt.ylabel('키',color='red',loc='top')

# 그래프 간격눈금 표시
plt.xticks([1,2,3])
plt.yticks([192,193,194,198])

# 

plt.show()

