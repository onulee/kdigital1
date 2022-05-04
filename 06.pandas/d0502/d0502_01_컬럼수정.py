import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 컬럼수정
# 1. 컬럼의 데이터를 비교해서 컬럼의 값을 변경하는 방법 - replace
# df['학교'].replace({'구로고':'단지고','디지털고':'상생고'},inplace=True)
# df['국어'].replace({100:190},inplace=True)

# 2. 컬럼전체를 변경 - 전체를 소문자변경
# df['SW특기'] = df['SW특기'].str.lower() # 소문자
# df['SW특기'] = df['SW특기'].str.upper() # 대문자
# df['SW특기'] = df['SW특기'].str.capitalize() # 첫글자 대문자
# df['SW특기'] = '합격'
# df['SW특기'].replace({'Java':'javaC'},inplace=True)
# df['학교'] = df['학교']+'등학교'
# 키  180 + cm
# 타입이 다를경우 에러 : +가 되지 않음. 형변환을 해줘야 함. astype함수
df['키'] = df['키'].astype(str) + 'cm'
print(df)

# 3. 다른 컬럼의 값을 비교해서 컬럼의 데이터를 변경
# filt = df['키']>=190
# df.loc[df['키']>=190,'국어']=100
# df['국어'] = 100
# print(df)

# row index를 가지고 row데이터 수정
# df.loc['4번','SW특기'] ='Python'
# row의 2개컬럼값을 변경
# df.loc['4번',['학교','SW특기']] =['가산고','Python'] 

# 문제 1.
# 강태원 학생 국어점수가 40점이면 50점으로 변경
# filt = (df['이름']=='강태원') & (df['국어'] ==40)
# df.loc[filt,'국어'] = 50
# df.loc['2번','국어'] = 50

# 문제 2.
# 국어점수가 40점이면 50점으로 변경    
# df['국어'].replace({40:50},inplace=True)

# # 문제 3.
# filt = (df['이름']=='강태원') & (df['국어']==40)
# df.loc[filt,['영어','수학','과학','사회']] = [50,50,50,50]
# # 강태원 -> 국어점수가 40점이면 영어,수학,과학,사회 모두 40점

# print(df)




