import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df.describe())  # 평균, 표준편차, 최소값, 최대값, 값분포도

print("키 최소값 : ",df['키'].min())
print("키 최대값 : ",df['키'].max())
print("키 평균 : ",df['키'].mean())
print("키 개수 : ",df['키'].count())
print("키 합계 : ",df['키'].sum())

print(df['키'].nlargest(3))  #큰사람 3명 출력
print(df['키'].nsmallest(3)) # 작은사람 3명 출력

print(df)
print("학교 : ",df['학교'])
# unique 중복제거 출력
print("학교 : ",df['학교'].unique())
# nunique 중복제거 숫자 출력
print("학교 : ",df['학교'].nunique())

#----------------------------------------------

# df = pd.read_excel('stat_142801.xls',skiprows=2,nrows=2) 
# print(df)
# print(df[df.columns[-1]])
# print(df['2020'])
# print(df.columns)

#----------------------------------------------

# df = pd.read_excel('score.xlsx')
# ## 컬럼 활용 
# print(df.columns)
# print(df.columns[0])
# print(df.columns[5])
# print(df.columns[-1])
# print(df[['이름','사회','SW특기']])
# print(df['SW특기'])
# print(df[df.columns[-1]])

#----------------------------------------------

# # index 지정 활용

# df.set_index('이름',inplace=True)
# print(df.index)  # index지정된 컬럼 출력
# print(df.index[0])
# print(df.index[5]) # 박동현
# print(df.loc['박동현'])
# print(df.loc[df.index[5]])
# print(df)
# print(df.index[-1]) # 마지막 index이름출력
# print(df.loc[df.index[-1]]) # 마지막 row출력
# print(df.tail(1))
# print(df.iloc[3:5])

#----------------------------------------------

# 1000개 출력일때 중간부분 skip해서 출력되지 않음. 중간부분 출력할수 있음.
# df = pd.read_excel('user.xlsx')
# print(df)
# print(df.iloc[500:505])
