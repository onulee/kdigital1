import pandas as pd

# 컬럼의 선택
df=pd.read_excel('score.xlsx',index_col='지원번호')

# 컬럼의 모두 출력
print(df.columns)
print(df.columns[0])  # 컬럼만 출력하기 위한 명령어
print(df.columns[2])

# 컬럼의 내용을 출력
# print(df['이름'])     # 컬럼 전체를 출력하는 명령어
# print(df[df.columns[-1]]) # 마지막 컬럼 전체를 출력
print(df['학교'])
print(df[['학교','국어']])  # 컬럼2개 내용을 출력할때 [[]]대괄호2개
print(df.columns[[1,3,-1]]) # 컬럼title 3개를 출력할때 [[]] 대괄호 2개
print(df[df.columns[[1,3,-1]]])  # 컬럼title을 가지고 컬럼내용 출력

print(df['영어'])
print(df['영어'][0:3]) #영어컬럼의 내용 row 5개 출력
print(df[['이름','영어']][0:5]) #영어컬럼의 내용 row 5개 출력
# print(df[0:5])  # 컬럼내용 row 5개 출력
# print(df[:3]) # 0부터 3이전까지 출력
# print(df[4:]) # 4부터 끝까지 출력


# print(df[5])  # 1개 출력시 df.iloc[5]
# print(df.iloc[0:5]) # row출력시 iloc,loc 사용
