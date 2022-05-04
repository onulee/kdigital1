import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)

# 그룹: 학교-학교명
# print(df.groupby('학교').get_group('구로고'))
# print(df.groupby('학교').get_group('디지털고'))

# 그룹: 학교, 평균지정하면 계산이 가능한 모든 컬럼의 학교별 평균을 구해줌
# print(df.groupby('학교').mean())

# 그룹 : 학교별 인원
# print(df.groupby('학교').size())  # 학교별 인원
# print(df.groupby('학교').size()['구로고']) # 학교별 구로고 인원
# print(df.groupby('학교').size()['디지털고']) # 학교별 디지털고 인원

# 그룹 : 학교 키컬럼만 평균
# print(df.groupby('학교')['키'].mean())
# 그룹 : 학교 수치가 가능한 모든컬럼 평균
# print(df.groupby('학교').mean())

# 그룹 : 학교 키,국어컬럼만 출력
# print(df.groupby('학교')[['키','국어']].mean())


