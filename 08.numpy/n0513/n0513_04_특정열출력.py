import numpy as np

# arr = np.arange(6).reshape(2,3)
arr = np.arange(25).reshape(5,5)
# print(arr)
# shape : 튜플(2,3) shape[0]:행, shape[1]:열
# print(arr.shape[0]) # 행
# print(arr.shape[1]) # 열

# 전체 행을 출력
print(arr[0])
print(arr)
# 특정열,전체 출력  arr[:,0] - x좌표는 모든것을 선택, y좌표는 0 선택 
print(arr[:,0])
print(arr[:,3])




# # 행의 길이
# print(len(arr))

# # 열의 길이
# print(len(arr[0]))


# list_data = [
#     [0,1,2],
#     [3,4,5]
# ]

# # 행의 길이
# print(len(list_data))

# # 열의 길이
# print(len(list_data[0]))

# 1차원 list 길이 : len(lst)
# lst = [0,1,2,3,4,5]
# print(len(lst))