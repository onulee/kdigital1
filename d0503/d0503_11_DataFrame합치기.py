import pandas as pd

# DataFrame Join
# concat 행기준으로 - 각각의 DataFrame 합침
# df = pd.concat([data1,data2,data3])

# 2차원데이터
data ={
    '이름':['주바다','공유진','송선유','양홍욱'],
    '키':[180,182,188,179],
    '몸무게':[47,49,50,45]
}

data2={
    '이름':['주바다','공유진','송선유','윤상운'],
    '전공':['컴퓨터공학','매카닉공학','독일어학','컴퓨터공학'],
    '실력':['고급','중고급','특급','중고급']
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

### DataFrame join하는 방법 
### merge - 열기준(이름)으로 합침 
# inner - data,data2 같은 데이터가 있는 경우만 합침
# df = 주바다,공유진,송선유,양홍욱
# df2 = 주바다,공유진,송선유,윤상운
mdf = pd.merge(left=df,right=df2, how='inner',on='이름')
print(mdf)

# left=df 기준으로 합침
mdf2 = pd.merge(left=df,right=df2, how='left',on='이름')
# mdf2['전공'][3]='자율전공'
# mdf2['실력'][3]='초급'
print(mdf2)

# right=df2 기준으로 합침
mdf3 = pd.merge(left=df,right=df2,how='right',on='이름')
print(mdf3)

# df,df2의 모든 열 합침
mdf4 = pd.merge(left=df,right=df2,how='outer',on='이름')
print(mdf4)



# 1차원 데이터
# temp = pd.Series([-20,-10,10,20])

# 2차원 데이터
# data = {
# '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
# '학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
# '키' : [197, 184, 168, 187, 188, 202, 188, 190],
# '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
# '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
# '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
# '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
# '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
# 'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
# }

# df = pd.DataFrame(data)
# print(df)