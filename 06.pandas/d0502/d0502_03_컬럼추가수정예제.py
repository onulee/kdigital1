import pandas as pd

# 상단 2개는 삭제
# 컬럼추가 
# 사고건수, 사망자수, 부상자수 , 교통사고 피해수 (사망자수+부상자수)
df = pd.read_excel('2020년월별교통사고01.xlsx',skiprows=2,index_col='월')
# print(df)
# print(df.index)    # index출력
# print(df.columns)  # 컬럼출력
# # 컬럼추가
# df['교통사고피해자수'] = df['사망자수(명)']+df['부상자수(명)']
# print(df)
# # row 합계 추가
# df.loc['합계'] = [df['사고건수(건)'].sum(),df['사망자수(명)'].sum(),df['부상자수(명)'].sum(),df['교통사고피해자수'].sum()]
# # row평균 추가
# df.loc['평균'] = [df['사고건수(건)'][:-1].mean(),df['사망자수(명)'][:-1].mean(),df['부상자수(명)'][:-1].mean(),df['교통사고피해자수'][:-1].mean()]
# print(df)

# # 사고건수가 평균보다 낮은 row의 값은 삭제하시오.
# print(df['사고건수(건)']['평균'])

# # filt = df['사고건수(건)'] < df['사고건수(건)']['평균']
# # 해당사항에 맞는 것만 출력


### 평균사고건수보다 낮은 것을 제외하고 row출력
# filt = df['사고건수(건)'] < df['사고건수(건)'].mean()
# df.drop(index=df[filt].index,inplace=True)
# print(df)


### 사망자수가 230미만 row삭제
filt = df['사망자수(명)'] < 230
df.drop(index=df[filt].index,inplace=True)
print(df)