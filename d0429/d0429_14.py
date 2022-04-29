import pandas as pd

df = pd.read_excel('시가총액1-200.xlsx')
print(df)

# 이름으로 순차정렬
print(df.sort_values('종목명'))

df = pd.read_excel('user.xlsx')
print(df)

print(df.sort_values('first_name',ascending=False))

# gender 순차정렬, frist_name역순정렬
print(df.sort_values(['gender','first_name'],ascending=[True,False]))

