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

# 그룹 : 학교,학년 2개컬럼, 정렬
# print(df.groupby(['학교','학년']).mean())

# 그룹 : 학교,학년 키 컬럼기준 몇명 인지 출력
# print(df.groupby(['학교','학년'])['키'].count())

# 그룹 : 학교,학년 - 점수 합계
# print(df.groupby(['학교','학년']).mean()) #평균
print(df.groupby(['학교','학년']).sum())    #합계
# 그룹 - 학교 , 합계 정렬
print(df.groupby(['학교']).sum().sort_values('국어'))

# 그룹 - 학교, sw특기 컬럼만 출력 : nan데이터는 count를 하지 않음
# print(df.groupby('학교')['SW특기'].count())

# 그룹 - 학교기준, 모든 컬럼 개수출력
# nan데이터 포함되어 있으면 개수가 더해지지 않음
print(df.groupby('학교').count())

# nan 데이터 출력
# filt = df['SW특기'].isnull()
# print(df.loc[filt,'SW특기'])