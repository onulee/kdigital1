import pandas as pd

# 연령별인구현황 엑셀파일 출력
# 상단부분 3줄 제외, 컬럼 : A제외, C,D제외, B,E~Y까지 출력
df = pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,E:Y')
print(df)
print(df.columns)
print(df['0~4세'])

# str.replace함수 적용 : 천단위, 삭제, int형변환
df['0~4세'] = df['0~4세'].str.replace(',','').astype(int)
print(df['0~4세'])
# 컬럼 0~4세 전국부분 제외후 합계
print(df['0~4세'][1:].sum()) 
print(df.info())





# movie.xlsx 불러와서 최대관객수 출력
# df = pd.read_excel('movie.xlsx')
# print(df['관객 수'].sum())

# print(df.info())



# print(df.index)
# print(df.loc[df.index[0]])

# print(df.loc['전국  '])








# movie.xlsx 불러와서 최대관객수 출력
# df = pd.read_excel('movie.xlsx')
# print(df)
# print(df.columns)

# print(df['관객 수'].sum())
# print(df['관객 수'].max())

# # 영화, 개봉연도만  3개 출력
# print(df[['영화','개봉 연도']][0:3])

# data = {
# '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
# '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
# '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
# '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
# }

# df = pd.DataFrame(data)
# df.to_excel('movie.xlsx',index=False)
# print(df)