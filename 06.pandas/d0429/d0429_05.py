import pandas as pd

df = pd.read_excel('score.xlsx',index_col="지원번호")
# rows loc함수
# print(df.loc[['1번','2번']])
print(df)
# 배열번호로 row검색출력
# print(df.iloc[0:5])
# print(df.iloc[3:7])
# print(df.loc['4번':'7번'])
# print(df.iloc[3:7,2])
# 4번째 학생, 0,1,2,3,4 지원번호 5번인 학생의 index제외하고
# 0:이름, 1:학교, 2:키 지원번호가 5번인 학생의 키값을 출력
print(df.iloc[4,2])
# 지원번호가 1번인 학생의 영어점수 출력
print(df.iloc[0,4])

# 2개이상 row출력시 대괄호 사용 , column 2개이상 대괄호 사용
print(df.iloc[[0,2],[0,2]])

# 슬라이싱 [] 1개 앞쪽 row, 뒤쪽 column
print(df.iloc[3:5,3:7])