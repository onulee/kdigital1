import pandas as pd

df = pd.read_excel('user.xlsx',index_col='id')
print(df)
print(df.columns)
print(df.index)

# 500~600,605 row출력
# id가 500~600,605번, first_name,email출력

