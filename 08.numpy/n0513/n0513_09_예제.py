import numpy as np

# [[1,1],[0,1]] (2,2)행렬,  
# [[2,0],[3,4]] (2,2)행렬, 
# 두행렬의 곱셈의 결과와
# 단위행렬 곱을 구하시오.
arr1 = np.array([[1,1],[0,1]])
arr2 = np.array([[2,0],[3,4]])
arr3 = arr1*arr2
print(arr3)
arr4 = np.dot(arr1,arr2)
print("-"*30)
print(arr4)

# 1부터 6까지 (2,3)행렬 + 7부터 12까지 (3,2) 행렬 
# 단위행렬 곱을 구하시오.
arr5 = np.arange(1,7).reshape(2,3)
arr6 = np.arange(7,13).reshape(3,2)
arr7 = np.dot(arr5,arr6)
print("-"*30)
print(arr7)

# 1부터 9까지 (3,3) 행렬을 만들고, 
# 1행줄 전체 x2, 2행줄 전체 x3을 해서 출력하시오
arr8 = np.arange(1,10).reshape(3,3)
print(arr8)
arr8[1] = arr8[1]*2  # 1행전체 * 2
arr8[2] = arr8[2]*3  # 2행전체 * 3
print(arr8)



# arr = np.arange(6)
# arr2 = np.arange(6)
# print(arr)
# # shape(6,) shape(6,)  1행 * 1 = 1개만 존재
# print(arr.shape)
# print(np.dot(arr,arr2))