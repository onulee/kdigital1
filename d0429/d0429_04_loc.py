# google_movie 4,5번 -> 제목,가격 출력하시오.

import pandas as pd

df = pd.read_excel('google_movie.xlsx',index_col=0)
df.index.name='번호'
print(df.index)

print(df.loc[[3,4],'가격'])
df.loc[[3,4],'가격']=1000
print(df.loc[[3,4],'가격'])