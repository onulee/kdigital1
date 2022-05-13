import numpy as np

arr1 = np.arange(8).reshape(2,4)
arr2 = np.arange(8).reshape(2,4)

# 행기준으로 합치기
arr3 = np.concatenate([arr1,arr2],axis=0)
print(arr3)

# 2차원행렬
arr4 = np.arange(4).reshape(4,1)
print(arr4)

# 서로다른 행렬의 더하기 연산
result_arr = arr3+arr4
print(result_arr)

