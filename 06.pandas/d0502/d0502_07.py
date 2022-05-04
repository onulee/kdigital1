import pandas as pd

df = pd.read_excel('user.xlsx',index_col='id')
print(df)

df['total'] = 0
print(df)

# 500,550,601:700,900,950

df['total'][500,505,900,950]=100
df['total'][601:700]=100
print(df.head(500))