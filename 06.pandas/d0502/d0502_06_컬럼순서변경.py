import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# print(df['지원번호']) #index설정 되어 있으면 columns 검색
### row추가
df.loc['9번'] = ['이순신','디지털고',200,100,100,70,90,80,'java'] 
print(df)

# 1명row값 변경
# df.loc['4번','SW특기'] = 'python'
### 4번,5번 2명 학생 값 변경
# df.loc[['4번','5번'],'SW특기'] = 'python'
### 1명의 row 2개의 컬럼을 변경할때
# df.loc['4번',['키','국어']] = [200,100]
# print(df)

### 컬럼의 순서를 변경
# - 컬럼추가
df['총합'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['결과'] = '불합격'
# - 컬럼수정
df.loc[df['총합']>400,'결과']='합격'
print(df)

# 컬럼순서 변경할때 list형태로 입력하면 컬럼순서가 변경.
# cols = ['이름','총합','학교','결과']
# print(df[cols])

# columns를 list타입으로 변경
cols = list(df.columns)

# 이름,학교,결과,총합,키,국어,영어,수학,과학,사회
# 0    1    -1  -2   2    3   4   5    6   7

# cols[0:2] # 이름,학교
# cols[-1] # 결과
# cols[-2] # 총합
# cols[2:8]  # 키,국어,영어,수학,과학,사회
#  list + int + int + list
df = df[cols[0:2]+[cols[-1]]+[cols[-2]]+cols[2:9]]
# print(df[['이름','학교','결과','총합','키','국어','영어','수학','과학','사회','SW특기']])
print(df)





