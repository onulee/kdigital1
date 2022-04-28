# 연령별인구현황 여자부분 출력
# 행정기관, 0~4세 - 100세이상까지 출력
# 제일 마지막 컬럼 1개 : 100세이상의 합계를 구하시오.
import pandas as pd

# 연령별인구현황 엑셀파일 출력
# df = pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,AB:AV')
# 중간특수문자 사이띄우기 안보임.
# print(df.columns)
# 컬럼명 상세보기
# 중간특수문자 사이띄우기 보임
# print(df.columns.values)

# 컬럼명 변경
# df.rename(columns={'100세 이상.1':'100세 이상'},inplace=True)
# print(df.columns.values)

df_m = pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,E:Y')
# print(df_m.columns)
df_m.set_index('행정기관',inplace=True)
# print(df_m)
# print(df_m.index)

# index 명칭 공백제거
# print(df_m.index[0].strip())

# index명칭 변경
df_m.rename(index={df_m.index[0]:df_m.index[0].strip()},inplace=True)
print(df_m.index)

# 연령별인구현황 엑셀파일 출력
# df_w = pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,AB:AV')
# print(df_w.columns)
# df_w.columns = df_m.columns
# print("-"*50)
# print(df_w.columns)



# print(df_w['100세 이상'][1:])
# # print(df.info())
# df_w['100세 이상'] = df_w['100세 이상'].str.replace(',','').astype(int)
# print('{:,d}'.format(df_w['100세 이상'][1:].sum()))

