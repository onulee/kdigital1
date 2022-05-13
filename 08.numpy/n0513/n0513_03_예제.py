# 1. 행렬 조건 
# 랜덤(randn)으로 (4,4)행렬을 만들고, 
# 0보다 큰 행렬은 2, 작은 행렬은 -2로 변경하시오.

# 2. 행렬2개를 만들어서 합치기
# 1부터 11까지 홀수 (3,2) 행렬 생성, 
# 2부터 12까지 짝수 (3,2) 행렬 생성후
# 행으로 결합하시오.

# 3. 행렬 분리
# 0부터 99까지 (10,10) 행렬을 만든후, 
# 3열을 기준 2개의 행렬로 분리하시오.

import numpy as np

# 1. 행렬 조건 
# 랜덤(randn)으로 (4,4)행렬을 만들고, 
# 0보다 큰 행렬은 2, 작은 행렬은 -2로 변경하시오.

# 랜덤 표준정규분포 난수 (양수,음수)
arr = np.random.randn(4,4)
print(arr)
# 0보다 큰 행렬은 2, 작은 행렬은 -2 
arr2 = np.where(arr>0,2,-2)
print(arr2)

# 2. 행렬2개를 만들어서 합치기
# 1부터 11까지 홀수 (3,2) 행렬 생성, 
# 2부터 12까지 짝수 (3,2) 행렬 생성후
# 행으로 결합하시오.
# 1,3,5,7,9,11
arr3 = np.arange(1,12,2).reshape(3,2)
# 2,4,6,8,10,12
arr4 = np.arange(2,13,2).reshape(3,2)
# 행으로 합치기
arr5 = np.concatenate([arr3,arr4],axis=0)
print(arr5)
# 열로 합치기
arr6 = np.concatenate([arr3,arr4],axis=1)
print(arr6)

# 3. 행렬 분리
# 0부터 99까지 (10,10) 행렬을 만든후, 
# 3열을 기준 2개의 행렬로 분리하시오.

arr7 = np.arange(100).reshape(10,10)
# 열기준으로 짜르기
left_arr,right_arr = np.split(arr7,[3],axis=1)
print(left_arr)
print(right_arr)

# 행기준으로 짜르기
top_arr,bottom_arr = np.split(arr7,[5],axis=0)
print(top_arr)
print(bottom_arr)

