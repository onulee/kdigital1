import numpy as np

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr3 = np.concatenate([arr1,arr2])
# print(arr3) # 1차원행렬
# # reshape행렬을 변경 : 2X3 2차원행렬생성
# arr4 = arr3.reshape((2,3))
# print(arr4)


# # reshape 행렬형태를 변경
# arr1 = np.arange(1,10)
# arr2 = arr1.reshape((3,3))
# print(arr2)

# # 2행5렬의 행렬생성
# arr3 = np.arange(1,11).reshape((2,5))
# print(arr3)

# arr4 = np.arange(20).reshape((4,5))
# print(arr4)

# arr5 = np.linspace(1,20,10).reshape((5,2))
# print(arr5)

# arr = np.arange(12).reshape((3,4))
# arr = np.arange(12).reshape(4,3)
# print(arr)

arr1 = np.arange(12)
arr2 = np.arange(15)

# reshape(3,-1) -1 : 지정한 행렬크기에 따라 열의 크기를 맞춰서 생성
# arr3 = arr1.reshape(3,-1)
# arr4 = arr2.reshape(3,-1)
# arr4 = arr2.reshape(3,-1)
# print(arr3)
# print(arr4)

# reshape -1은 변동형으로 행렬을 생성
arr3 = arr1.reshape(-1,6)
print(arr3)

arr4 = arr2.reshape(-1,5)
print(arr4)





