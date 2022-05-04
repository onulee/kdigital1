import pandas as pd
# data : dic타입
data = {
'이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
'학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
'키' : [197, 184, 168, 187, 188, 202, 188, 190],
'국어' : [90, 40, 80, 40, 15, 80, 55, 100],
'영어' : [85, 35, 75, 60, 20, 100, 65, 85],
'수학' : [100, 50, 70, 70, 10, 95, 45, 90],
'과학' : [95, 55, 80, 75, 35, 85, 40, 95],
'사회' : [85, 25, 75, 80, 10, 80, 35, 95],
'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
df.index.name='지원번호'
# print(df)
df.reset_index(drop=True,inplace=True)
# print(df)
df.set_index('이름',inplace=True)
# print(df)
df.reset_index(inplace=True)
# print(df)
# 이름index 삭제, index추가, 지정

# 컬럼을 추가 - 없는이름을 삽입하면 컬럼추가
df['지원번호'] = ['1번','2번','3번','4번','5번','6번','7번','8번']
print(df)

df.set_index('지원번호',inplace=True)
print(df)
# index지정 출력
print(df.index)
# row index 출력
print(df.loc['7번'])
# print(df.iloc[6])

# 모든 컬럼 출력
# print(df.columns)
# print(df[['이름','키']])




