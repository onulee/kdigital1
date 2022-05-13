import numpy as np

# 행렬 합치기 : np.concatenate
# 행렬 나누기 split
arr = np.arange(8).reshape(2,4)
print(arr)

# (2,2),(2,2)행렬로 나누기 : split
# 0,1,2,3
# split(행렬,기준위치,행열기준axis)
# left,right = np.split(arr,[2],axis=1)
# print(left)
# print(left.shape)
# print(right)
# print(right.shape)

# 0,1,2,3 ->열 1의기준으로 행렬을 나눔.
# left,right = np.split(arr,[1],axis=1)
# print(left)
# print(right)

# 행 0,1 ->행 1의 기준으로 행렬을 나눔.
top,bottom = np.split(arr,[1],axis=0)
print(top)
print(bottom)
