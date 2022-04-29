import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')

# 조건출력 - True, False
print(df['키']>180)

# 변수선언
filt = df['키']>188

# 조건변수를 입력하면 조건에 맞는 것만 출력
print(df[filt])

# 바로 조건식을 삽입
print(df[(df['키']>188)])
# 조건식 not : ~
print(df[~(df['키']>188)])

# row출력에서 컬럼1개, 여러개 출력
print(df.loc[(df['키']>188),'학교'])
print(df.loc[(df['키']>188),['이름','국어','영어']])
# print(df.loc[['1번','5번'],['이름','국어','영어']])

# and조건식 : & 대한 조건 활용 
print(df.loc[(df['키']>=185)&(df['학교']=='구로고'),['학교','사회']])
# 학교,국어,영어,수학,사회 컬럼까지 출력
# print(df.loc[(df['키']>=185)&(df['학교']=='구로고'),'학교':'사회'])

# or 조건식 : | 대한 조건 활용
print(df.loc[(df['키']<170) | (df['키']>200),['이름','학교','키']])





# print(df.iloc[[0,3],[0,2]])