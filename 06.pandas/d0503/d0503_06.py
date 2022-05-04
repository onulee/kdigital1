import pandas as pd

df = pd.read_csv('전체연봉.csv')

# null데이터 출력
filt = df['WAR'].isnull()
# print(df[filt])

# 1. WAR컬럼에 nan데이터를 0으로 대체
# index순서대로 column을 수정
df.loc[filt,'WAR'] = 0

# 2. WAR컬럼에 nan데이터를 0으로 대체
# df['WAR'].fillna(0,inplace=True)
# print(df)

# nan 데이터 인 애플러 2022 검색
# filt2 = (df['선수']=='애플러') & (df['연도']==2022)
# print(df[filt2])

# print(df.groupby('선수').mean())
# print(df.sort_values('선수'))

print(df.groupby('연도')['연봉(만원)'].mean())
print(df.groupby('연도').count())
print(df.groupby('연도').size())
