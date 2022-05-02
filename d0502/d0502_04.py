import pandas as pd

# 상단 2개는 삭제
# 컬럼추가 
# 사고건수, 사망자수, 부상자수 , 교통사고 피해수 (사망자수+부상자수)
df = pd.read_excel('2020년월별교통사고01.xlsx',skiprows=2,index_col='월')
print(df)




# df[컬럼][index]
# print(df['사고건수(건)'][1:3])
# print(df.iloc[0:-1])