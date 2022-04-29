import pandas as pd

df = pd.read_excel('user.xlsx')

# de포함되어 있는 이름을 검색하시오. 대소문자 구분 없음.
# 개수 54개
filt = (df['first_name'].str.contains('de')|df['first_name'].str.contains('De'))
# print(df[filt])


# case=False 이면 대소문자 구분없음. Nan처리 : na=True, na=False, Nan 
filt = (df['first_name'].str.contains('de',case=False,na=False))
print(df[filt])


# # isin list 타입이 들어올수 있음.
df = pd.read_excel('score.xlsx')
print(df)

# Nan - False처리해서 출력제외, case=False 대소문자 구문없음
filt = df['SW특기'].str.contains('python',case=False,na=False)
print(filt)
print(df[filt])


# print(df['SW특기'])
# isin 해당되는 글자가 있는지 확인해서 출력
# langs = ['python','java']
# filt = df['SW특기'].str.lower().isin(langs)
# print(df[filt])


# De시작하는 이름을 검색하시오. 
# filt = df['first_name'].str.startswith('De')
# print(df[filt])
