# 가장 주문을 많이 한 상품 5개를 출력
# item_name당 주문 개수(order_id)와 총량(합계, quantity)을 출력
# order_id 주문당 평균 계산금액을 출력

import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# df = pd.read_excel('score.xlsx')
# df['학년']=[3,3,2,1,1,3,2,2]

# v_count = df.groupby('학교')['학년'].value_counts()
# print(v_count)
# print(df)

df = pd.read_csv('chipotle.tsv',sep='\t')
# print(df)
print(df.shape)
print(df.describe())
print(df.info())

# 의미없는 숫자를 문자처리 - order_id를 숫자로 인식해서 계산을 함.
df['order_id'] = df['order_id'].astype(str)
print(df.info())

## 1. 가장 주문을 많이 한 상품 5개출력 - 상품별 count
## item_name 으로 count
item_count = df['item_name'].value_counts()[:5]
print(item_count)

# 2. 총주문수
print("총주문수 : ",len(df['order_id'].unique()))

# 2. 1)주문이 들어온 상품 50개, 중복제거 item_name 출력 - 50개 출력
print(df['item_name'].unique()) # 주문한 메뉴종류
# 2. 2) 주문한 메뉴 종류의 수
print("주문한 메뉴종류수 : ",len(df['item_name'].unique())) # 주문한 메뉴종류 수


# 3. 1)item_name당 총주문수 - 주문이 많은 순으로 출력
item_count = df['item_name'].value_counts()
for idx, (val, cnt) in enumerate(item_count.iteritems()):
    print("주문", idx, ":", val, cnt)

### 3. 1)item_name당 총주문수 - 순서대로 출력   
order_count = df.groupby('item_name')['order_id'].count()
order_count[:10] # item당 주문 개수를 출력합니다.    
print(order_count[:10])  

# 3. 2) item_name당 주문 총량을 출력
item_quantity = df.groupby('item_name')['quantity'].sum()
item_quantity[:10] # item당 주문 총량을 출력
print(item_quantity[:10])

# 4. order_id 주문당 평균 계산금액을 출력 
# column 단위 데이터에 apply 함수로 전처리를 적용.
df['item_price'] = df['item_price'].apply(lambda x: float(x[1:]))
df.describe()

df.groupby('order_id')['item_price'].mean()
print(df.groupby('order_id')['item_price'].mean())
# print(df.groupby('order_id')['item_price'].sum().mean())


# 5. 막대그래프
# 3. 2) item_name당 주문 총량을 출력
item_quantity = df.groupby('item_name')['quantity'].sum()
# 이름 출력
print(item_quantity.index)
print(len(item_quantity.index)) # 개수

x_arr = np.arange(len(item_quantity.index))

# 번호로 출력
# plt.bar(x_arr,item_quantity)
# x축 item_name으로 출력
plt.bar(item_quantity.index,item_quantity)
plt.ylabel('주문량')
plt.title('주문량 그래프')

plt.show()








# 1. 가장 주문을 많이 한 상품 5개를 출력하시오.
# value_counts()

# 2. 총주문수를 출력하시오.
# 1). 주문한 메뉴(item_name)의 종류를 출력하시오.
#unique
# 2). 주문한 메뉴(item_name) 종류의 수를 출력하시오.
# len
# 3. item_name당 주문 개수(order_id)와 총량(합계, quantity)을 출력하시오.
# item_name order_id 몇개인지 출력
# groupby('item_name')['order_id']
# item_name quantity 몇개 인지 출력
# groupby('item_name')['quantity']

# 4. order_id 주문당 평균 계산금액을 출력하시오.

# ------------------------------------------------------------------------------

# 5. 막대그래프로 표현하시오.
# 메뉴item_name의 주문개수를 그래프로 출력하시오.
# ( title : 주문량 그래프
# ylabel : 주문량, xlabel:주문번호order_id,item_name )

# df = pd.read_csv('chipotle.tsv',sep='\t’)



