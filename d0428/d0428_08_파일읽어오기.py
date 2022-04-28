import pandas as pd

#csv파일 읽어오기, index_col 지원번호를 index지정
# skiprows는 1번째줄을 삭제후 가져옴.
# df = pd.read_csv('score.csv',skiprows=1)
# print(df)
# print(df.index)

#csv파일 읽어오기, index_col 지원번호를 index지정
# skiprows는 상위 2줄을 제외후 가져오기
# skiprows는 [0,1,3,5] 0,1,3,5번째 줄은 제외하고 가져오기
# nrows는 개수만큼 가져오기 - 1번째줄은 컬럼
df = pd.read_excel('stat_142801.xls',skiprows=[0,1,3,5],nrows=2,index_col=0)
print(df)
# print(df['2020']) #컬럼 출력
# print(df.index)
# print(df.loc['출생아 수']) # row출력





#txt파일 읽어오기
# df = pd.read_csv('score.txt',sep='\t',index_col='지원번호')
# print(df)
# print(df.index)

# excel 파일 읽어오기
# df = pd.read_excel('score.xlsx',index_col='지원번호') 
# print(df)
# print(df.index)

