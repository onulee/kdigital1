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

# stu1000.xlsx 파일 읽어와서
# 1. 합계,평균 컬럼을 추가
df['합계'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
# / 나누기 소수점., // 몫 - 소수점이 없음.
df['평균'] = (df['합계']/5).astype(int)
# print(df)

# 2. 학교컬럼 그룹으로 합계를 역순정렬하시오.
# print(df.groupby(['학교','학년']).sum().sort_values('합계',ascending=True))
# print(df.groupby(['학교','학년']).mean().sort_values('합계'))

# 카테고리별 개수 출력
print(df['학년'].value_counts())
# 전체 개수
print(df['학년'].count())
# 중복제거 출력
print(df['학년'].unique())  
print(df['SW특기'].value_counts())


