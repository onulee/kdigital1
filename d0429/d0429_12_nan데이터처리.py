import pandas as pd
import numpy as np
df = pd.read_excel('score.xlsx',index_col='지원번호')

# axis=index 해당되는 행삭제
# df.dropna(axis='index',inplace=True)
# nan이 있는 행(index) 삭제
# df.dropna()

# axis='columns' 해당되는 열삭제
# df.dropna(axis='columns',inplace=True)

df['학교']=np.nan

# how='any' nan 1개라도 있으면 삭제, 학교와 SW특기 컬럼 삭제
# df.dropna(axis='columns',how='any',inplace=True)

# how='all nan 모두 있어야 삭제, 학교 컬럼 삭제
# df.dropna(axis='columns',how='all',inplace=True)

print(df)


# nan데이터 처리
# df.fillna('없음',inplace=True)

# nan데이터 삭제
# df.dropna(inplace=True)
