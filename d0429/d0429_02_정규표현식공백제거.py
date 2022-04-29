import pandas as pd
import re

df=pd.read_excel('stat_142801.xls',skiprows=2,nrows=2,index_col=0)

print(df.index)
print(df.index.values)
print(df.loc['출생아\xa0수'])
for i in range(len(df.index)):
    # 한글만 남기고 모든 문자 제거
    # df.rename(index={df.index[i]:re.sub(r'[^ㄱ-힣]','',df.index[i])},inplace=True)
    # \d : 숫자를 [0-9]와 동일
    # \D : 숫자가 아닌 문자 [^0-9]와 동일
    # \s : 공백 문자(띄어쓰기, 탭, 엔터 등)
    # \S : 공백이 아닌 문자
    # \w : 알파벳대소문자, 숫자 [0-9a-zA-Z]와 동일
    # \W : non alpha-numeric 문자 [^0-9a-zA-Z]와 동일
    
    df.rename(index={df.index[i]:re.sub(r'[\s]','',df.index[i])},inplace=True)
print(df.index.values)


# print(df.loc['출생아 수'])



# df.rename(index={df.index[0]:re.sub([],'',df.index[0])},inplace=True)


# df.index.name='목록'
# print(df.index)
# print(df.index.values)
# print(df.loc[df.index[0]])
# print(df.loc['출생아\xa0수'])


# df.rename(index={'출생아\xa0수':'출생아수'},inplace=True)
# df.rename(index={'출생아\xa0수':'출생아수'},inplace=True)
# print(df.index.values)