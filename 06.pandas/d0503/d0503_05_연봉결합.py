import pandas as pd

data1 = pd.read_csv('2020년연봉.csv')
data2 = pd.read_csv('2021년연봉.csv')
data3 = pd.read_csv('2022년연봉.csv')
# print(data1)
# print(data2)
# print(data3)

# 컬럼하단부분으로 합침
df = pd.concat([data1,data2,data3])
print(df.head(101))

df.to_csv('전체연봉.csv',encoding='utf-8-sig',index=False)

# print(data2.sort_values(['WAR'],ascending=False))