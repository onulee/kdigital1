import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')

# 컬럼 삭제 : drop(columns)
# df.drop(columns=['국어'],inplace=True)
# df.drop(columns=['국어','영어','수학'],inplace=True)

##### row삭제
# row 1개 삭제 : drop(index)
# df.drop(index='3번',inplace=True)
# row 여러개 삭제
# df.drop(index=['1번','3번'],inplace=True)
# print(df)


#### row삭제
# 수학점수가 80점미만 삭제후 출력
filt = df['수학']>=80
print(df[filt].index)

# df.drop(index=['1번','2번'],inplace=True)
# df[filt].index를 넣어서 삭제가능
# df.drop(index=df[filt].index,inplace=True) #조건에 해당되는 것만 삭제
# print(df)








