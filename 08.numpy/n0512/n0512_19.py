import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

df = pd.read_excel('score.xlsx')
# df['학년']=[3,3,2,1,1,3,2,2]
x=df['이름']
y = np.random.randint(60,100,8)

plt.bar(x,y)
plt.ylim(50,100)
plt.show()