import pandas as pd

def result(score):
    if score>=90:
       result = 'A'
    elif score>=80:
        result='B'
    elif score>=70:
        result='C'
    elif score>=60:
        result='D'
    else:
        result = 'F'            
    return result

df = pd.read_excel('score.xlsx',index_col='지원번호')
# 1. 평가
# 사회점수평가 컬럼추가
# 90이상 A
# 80이상 B
# 70이상 C
# 60이상 D
df['사회평가'] = 'F'
df['사회평가'] = df['사회'].apply(result)

# 2. 컬럼순서 변경
# 사회점수, 사회점수평가 컬럼순서를 변경하시오.
# df.columns 컬럼명들을 list
cols = list(df.columns)
print(cols)
df = df[cols[0:8] + [cols[-1]] + [cols[8]]]
print(df)

# 3.국어,영어,수학,과학,사회 
# 합계, 평균 컬럼 생성
df['합계'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['평균'] = df['합계']/5


# 4. 평균에 따른 평균평가  컬럼추가
df['평균평가']='F'
df['평균평가'] = df['평균'].apply(result)
print(df)


