import pandas as pd
df_m = pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,E:Y',index_col='행정기관')
df = pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,AB:AV',index_col='행정기관')
print(df.columns)

# 컬럼title전체를 변경
df.columns = df_m.columns

# df_m.rename(index={df_m.index[0]:df_m.index[0].strip()},inplace=True)
# 1개 컬럼title명을 변경:rename
df.rename(columns={df.columns[0]:'4세'},inplace=True)
print(df.columns)
# for문 : df.index수 만큼 
for i in range(len(df.index)):
    # 빈공백 제거 : strip()
    # re.sub(korean,'',str)
    df.rename(index={df.index[i]:df.index[i].strip()},inplace=True)

print(df.index.values)



# df = pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,E:Y',index_col='행정기관')
# print(df)
# print(df.columns)
# print(df['0~4세'])
# # pandas 1차원데이터 여러개
# print(type(df['0~4세'])) #Series
# df['0~4세'] = df['0~4세'].str.replace(',','').astype(int)

# print(df['0~4세'][1:].sum())