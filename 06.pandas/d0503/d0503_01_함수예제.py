import pandas as pd
import random

df = pd.read_excel('score.xlsx',index_col='지원번호')

# 1. 요일컬럼 추가
df['요일'] = 0
# columns 컬럼 수정
# df['요일'][0] = 1
# df['요일'][1] = 2

# row loc index수정
# df.loc['1번','요일'] = 1
# df.loc['2번','요일'] = 2
# row iloc index수정
# df.iloc[0,9] =1
# for i in range(8):
#     df.iloc[i,9] =random.randint(0,6)




# # 컬럼 개수
# print(df.columns)
# print(len(df.columns))
# # row 개수
# print(df.index)
# print(len(df.index))

# 2. 0-6까지 숫자를 랜덤으로 입력 - 함수 만들어서 사용금지
# 1) 기본for문
# for i in range(8):
#     df['요일'][i] = random.randint(0,6)

# 2) 한줄for문
# df['요일'] = 뒤부분을 list타입을 입력하면 됨.
# df['요일'] =[1,2,3,4,5,6,1,2]
df['요일'] = [random.randint(0,6) for i in range(8)]

# 3. 함수생성
#    0-월, 1-화, 2-수.....6-일 입력
def result(temp):
    if temp==0:
        result = '월'
    elif temp==1:
        result = '화'
    elif temp==2:
        result = '수' 
    elif temp==3:
        result = '목' 
    elif temp==4:
        result = '금' 
    elif temp==5:
        result = '토' 
    else:
        result = '일'
    return result     
                                
df['요일'] = df['요일'].apply(result)

# 4. 요일 컬럼을 키 바로 뒤로 컬럼순서를 변경하시오.
# print(df.columns)
cols = list(df.columns)
df = df[cols[0:3]+[cols[-1]]+cols[3:-1]]
print(df)

print(df.columns)
print(df.shape)
print(df.shape[0])
print(type(df.shape[0]))
print(df.info())