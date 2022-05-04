import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)
# 컬럼수정 문자+문자 = 문자(o), 정수형 + 문자 = 불가능, 타입형변환
df['학교'] = df['학교']+'등학교'
print(df)

# 컬럼수정 정수형 + 정수형 = 정수형(o)
df['키'] = df['키'] + 100
print(df)

# 정수형 + 문자형 (X) 불가능, 정수형을 문자형으로 변경 후 더하기 실행
# astype(str) 형변환
# df['키'] = df['키'].astype(str) + 'cm'
# print(df)