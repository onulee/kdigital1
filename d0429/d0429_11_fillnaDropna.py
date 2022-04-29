import pandas as pd
import numpy as np

df = pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)

# nan데이터 처리
#------------------------------------
# 결측치 : Nan데이터 처리
# fillna : Nan데이터를 처리
# print(df.fillna('',inplace=True))
# print(df.fillna('없음',inplace=True))

df['학교'] = np.nan
# df['수학'] = np.nan
# 모든 nan값을 대체
# df.fillna('없음',inplace=True)

# 학교 컬럼만 nan을 대체
# df['학교'].fillna("없음",inplace=True)
# df['수학'].fillna(0,inplace=True)
print(df)

# nan데이터 삭제
#----------------------------------
# dropna -> 해당되는 행 삭제
df.dropna(inplace=True)

print(df)







# filt = df['SW특기'].str.contains('python',case=False,na=False)
# filt = df['SW특기'].str.contains('없음',case=False)
# print(filt)
# print(df[filt])