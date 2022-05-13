import numpy as np
import pandas as pd

# 각 국가별 획득한 메달 포인트의 합을 구하시오.
# ( 금메달 4포인트, 은메달 2포인트, 동메달 1포인트 )
# 단 메달 포인트 계산은 numpy를 활용
# DataFrame을 출력하시오.

# [ 메달 포인트 ]
# Russian Fed.  100
# Norway        99
# ...
# Kazakhstan    4

# 1. DataFrame 생성
# 컬럼 : country_name,gold,silver,bronze
# 2. 메달 형태만 DataFrame을 분리해서 다시 생성
# 3. dot함수 사용해서 단위행렬 계산
# 4. 메달 포인트 [4,2,1] 생성
# 5. 나라명, 메달포인트를 가지고 DataFrame 생성
# 6. 출력

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

# DataFrame - dic타입
df = {'country_name':countries,
                        'gold': gold,
                        'silver': silver,
                        'bronze': bronze}


# DataFrame타입으로 변경
df = pd.DataFrame(df)
print(df)

# 컬럼3개 가진 df
medal_cnt = df[['gold','silver','bronze']]
print(medal_cnt)

# numpy타입으로 변경
point_arr = np.array([4,2,1])

# 단위행렬 곱으로 계산
# points = np.dot(medal_cnt,[4,2,1])
points = np.dot(medal_cnt,point_arr)
print(points)

# pandas DataFrame 컬럼 추가
df['points'] = points
print(df[['country_name','points']])

# 타입 출력
print(type(df['points']))

# 파일 저장
# df.to_excel('medal_points.xlsx')
