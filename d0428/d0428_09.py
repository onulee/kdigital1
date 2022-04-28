import pandas as pd

# excel파일 불러오기
df=pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)
print(df.iloc[0])  # rows index 출력 
print(df.index[3]) # index지정 3번째 출력 -> 지원번호 4번 
print(df.loc['2번'])  # rows index명으로 출력
print(df.index)    # index지정 모두 출력
print(df.loc[df.index[3]])  # rows index명으로 출력

# 숫자컬럼 최대값, 평균, 숫자 분포도 통계를 보여줌.
# print(df.describe())

# 컬럼의 타입
# print(df.info())

# df=pd.read_excel('user.xlsx')
# print(df)
# 컬럼 타입정보 - object,float,int
# print(df.info())
# 상위 5개만 보여짐. 10라는 숫자를 넣으면 10개 보여짐.
# print(df.head())
# print(df.head(10))

# 하위 5개만 보여짐
# print(df.tail())
# print(df.tail(20))

# 배열구조로 출력
# print(df.values)
# print(df.values[500:505])
# arr = df.values[0]
# print(type(arr))
# print(arr)

# 1개 row출력
# print(df.iloc[0])
# print(df.index)
# 1개 col출력
# print(df['first_name'])
# 2개 col출력
# print(df[['first_name','gender']])
# index 출력
# print(df.index)
# 컬럼 출력
# print(df.columns)
# row,column수를 출력
# print(df.shape)

# skiprows : 개수만큼 제외, nrows : 개수만큼 가져옴
# df = pd.read_excel('user.xlsx',skiprows=[i for i in range(0,500)],nrows=10) 
# print(df)