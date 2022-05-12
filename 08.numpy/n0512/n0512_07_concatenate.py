import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# 1차원행렬, 2차원 행렬 합치기
# 행렬합치기 concatenate 1차원 행렬은 axis=1기준으로 합침.
arr3 = np.concatenate([arr1,arr2])

print(arr3)
print(arr3.shape)