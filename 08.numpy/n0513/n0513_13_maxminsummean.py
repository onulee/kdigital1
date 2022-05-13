import numpy as np

# 1,9까지 (3,3)행렬을 생성후 행의 sum(행의 합), 열의 sum(컬럼의 합)을 출력하시오.
arr = np.arange(1,10).reshape(3,3)
print(arr)
# 컬럼의 합이 계산
axis0 = arr.sum(axis=0)
# axis0 = np.sum(arr,axis=0)
print(axis0)

# 행의 모든 값이 계산
axis1 = arr.sum(axis=1)
print(axis1)


# 집계함수
# max,min,sum,mean

# arr = np.array([[1,2],[3,4]])
# print(arr)

# # 2차원 행렬의 모든 수의 합
# arr_sum = np.sum(arr)
# print(arr_sum)


### 집계함수 2차원 sum
# 2차원 행렬의 컬럼의 합
# axis0_arr = np.sum(arr,axis=0)
# print(axis0_arr)

# # 2차원 행렬의 행의 합
# axis1_arr = np.sum(arr,axis=1)
# print(axis1_arr)


# 2차원행렬, 합
# arr_sum = np.sum(arr)
# print(arr_sum)
# arr_max = np.max(arr)
# print(arr_max)
# arr_min = np.min(arr)
# print(arr_min)
# arr_mean = np.mean(arr)
# print(arr_mean)




# arr = np.arange(16).reshape(4,4)
# print(arr)

# print("최대값 : ",np.max(arr))
# print("최소값 : ",np.min(arr))
# print("합계 : ",np.sum(arr))
# print("평균 : ",np.mean(arr))