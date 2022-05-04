import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 컬럼추가
# 없는 컬럼이름을 입력하면 컬럼추가
# df['총합']=0
df['총합']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['결과']='불합격'

# 컬럼수정 - 다른컬럼을 비교해서 자신의 컬럼값을 변경 df.loc
filt = df['총합']>400
df.loc[df['총합']>400,'결과']='합격'

print(df)
