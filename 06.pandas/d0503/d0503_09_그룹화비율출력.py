import pandas as pd
import numpy as np

def school(temp):
    if temp==1:
        result='구로고'
    elif temp==2:
        result='디지털고'
    else:
        result='단지고'
    return result    

def sw(temp):
    # SW특기 1-Java, 2-c, 3-Python 4-Javascript 5-JAVA
    if temp==1:
        result='Java'
    elif temp==2:
        result='c'
    elif temp==3:
        result='Python'
    elif temp==4:
        result='Javascript'
    else:
        result= np.nan
    return result                  

df = pd.read_excel('stu1000.xlsx',index_col='학번')
# 1,2,3으로 설정 -> 구로고,디지털고,단지고로 변경
# 1-구로고, 2-디지털고, 3-단지고
df['학교'] = df['학교'].apply(school)
# SW특기 1-Java, 2-c, 3-Python 4-Javascript 5-JAVA
df['SW특기'] = df['SW특기'].apply(sw)
# print(df)


### 그룹화 groupby
# 컬럼1개
# mean,count,sum
# 컬럼2개
# 그룹컬럼의 정렬
# 그룹화 출력시 컬럼개수선정 

# 1. index value 개수 출력
# result = df.groupby('학교')['학년'].value_counts()
# print(result)

# 2. index value 개수 출력
# result = df.groupby('학교')
# print(result['학년'].value_counts())

# 3. index value 개수 출력
# print(df.groupby('학교')['학년'].value_counts())

# 학교로 그룹화 후 구로고 학생 학년으로 학생수 확인
# print(df.groupby('학교')['학년'].value_counts())
print(df.groupby('학교').count())
# print(df.groupby('학교')['학년'].value_counts().loc['구로고'])

# normalize=True 개수가 아닌 (비율)로 출력
# temp = df.groupby('학교')['학년'].value_counts(normalize=True).loc['구로고']
# temp = df.groupby('학교')['학년'].value_counts(normalize=True)
# print(temp)
