import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 컬럼 전체출력
# print(df.columns)
# print(df.index)

# 전체컬럼 이름 변경
# df.columns=['name','school','height','kor'........]

### 컬럼이름을 변경 rename(columns)
# df.rename(columns={'이름':'name'},inplace=True)
df.rename(columns={'이름':'name','학교':'school'},inplace=True)
print(df)
