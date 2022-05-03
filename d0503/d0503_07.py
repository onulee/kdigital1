import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')

# 그룹
# print(df.groupby('학교').mean())

# 학년 컬럼 추가 - index크기 : 8개
# 컬럼추가 : index크기만큼 list로 추가해주면 됨.
df['학년'] =[3,3,2,1,1,3,2,2]
print(df)

# 1개컬럼 그룹화 - 학교
# df.groupby('학교').count()

# 2개컬럼 그룹화 - 학교, 학년을 가지고 그룹화 : 평균 수치가 가능한 모든 컬럼 표시
# print(df.groupby(['학교','학년']).mean())

# 2개컬럼 그룹화 - 개수
# print(df.groupby(['학교','학년']).count())

# 학년 그룹화 - 평균의 역순정렬
# print(df.groupby('학년').mean().sort_values('키',ascending=False))



