import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# ['order_id', 'quantity', 'item_name', 'choice_description','item_price']
# index:4622,컬럼:5
# 중복제거 order_id : 1834
# 주문한 메뉴 개수 : 50
df = pd.read_csv('chipotle.tsv',sep='\t')

# order_id -> 타입 변경
df['order_id'] = df['order_id'].astype(str)



# 주문한 메뉴 개수 : 50
print(len(df['item_name'].unique()))

#### 1. 가장 많이 주문한 item_name : value_counts()하면 됨.
# 자동으로 역순정렬이 되어서 출력이 됨.
item_count = df['item_name'].value_counts()
# item_count = df['item_name'].value_counts()[:10]
print(item_count)
print(item_count.shape)

# iteritems 2개의 열을 가져올수 있음
for i,(item_n,cnt) in enumerate(item_count.iteritems()):
   print("주문{} : ".format(i),item_n,cnt) 
   
# 2. 중복제거 후 order_id
print(df['order_id'].unique())
print('order_id 주문 : ',len(df['order_id'].unique()))
   
#### 3. item_name당 주문한 개수
order_count = df.groupby('item_name')['order_id'].count().sort_values(ascending=False)   
print(order_count)

### 3. item_name당 주문량 - quantity int타입, 수량을 더해서 가져와야 함.
item_quantity = df.groupby('item_name')['quantity'].sum().sort_values()
print(item_quantity)

### 4. order_id 주문당 평균 계산금액을 출력하시오.
# item_price str -> float 형변환
# lambda 간편함수정의
def fun(x):
  x = float(x[1:])
  return x
df['item_price'] = df['item_price'].apply(lambda x:float(x[1:]))
# df['item_price'] = df['item_price'].apply(fun)
print(df['item_price'])
df.groupby('order_id')['item_price'].sum().mean()

print("평균주문금액 : {:.2f} 달러".format(df.groupby('order_id')['item_price'].sum().mean()))