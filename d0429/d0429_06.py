import pandas as pd

df = pd.read_excel('user.xlsx',index_col='id')
print(df)
print(df.index)
print(df.columns)

# 조건을 사용해서 iloc 검색 500:600,605 출력
print(df.iloc[(df.index>=500) & (df.index<=600) | (df.index==605)])

# 500:600,605 frist_name,email 만 출력
# iloc검색
# print(df.iloc[(df.index>=500) & (df.index<=600) | (df.index==605),['first_name','email']])
# print(df.loc[(df.index>=500) & (df.index<=600) | (df.index==605)][['first_name','email']])
print(df.iloc[(df.index>=500) & (df.index<=600) | (df.index==605)][['first_name','email']])
# loc검색






# 500~600,605 row출력
# id가 500~600,605번, first_name,email출력
# print(df.iloc[[0,2],[0,2]])
# temp = (df.index>=500) & (df.index<=600) | (df.index==605)
# print(df.iloc[temp][['first_name','email']])


