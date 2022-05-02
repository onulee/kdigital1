import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 1. 평가
# 사회점수평가 컬럼추가
# 90이상 A
# 80이상 B
# 70이상 C
# 60이상 D

# 2. 컬럼순서 변경
# 사회점수, 사회점수평가 컬럼순서를 변경하시오.


# 3.국어,영어,수학,과학,사회 
# 합계, 평균 컬럼을 만들고

# 4. 평균에 따른 평균평가  컬럼추가



def result(score):
    # A,B,C,D,F 평가
    if score >= 90:
        temp = 'A'
    elif score >=80:
        temp = 'B' 
    elif score >=80:
        temp = 'C' 
    elif score >=80:
        temp = 'D'
    else:
        temp = 'F'     
                
    return temp

# 사회점수, 사회점수평가 컬럼순서를 변경하시오.