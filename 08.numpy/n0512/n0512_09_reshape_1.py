import numpy as np

# [ 문제 ]
# (5,10)의 행렬을 0부터 시작하여 2의 배수로 출력하시오.
arr1 = np.arange(0,100,2).reshape(5,10)
print(arr1)

# [ 문제 ]
# 1의 값을 (3,7)행렬을 출력하시오.
arr2 = np.ones(21).reshape(3,7)
print(arr2)


# arr = np.arange(12)
# reshape(-1,) 행은 변동, 열은 고정
# print(arr.reshape(-1,1)) # (12,1)
# print(arr.reshape(-1,2)) # (6,2)
# print(arr.reshape(-1,3)) #(4,3)
# print(arr.reshape(-1,4)) #(3,4)

# reshape(,-1) 행은 고정, 열은 변동
# print(arr.reshape(1,-1)) # (1,12)
# print(arr.reshape(2,-1)) # (2,6)
# print(arr.reshape(3,-1)) # (3,4)
# print(arr.reshape(4,-1)) # (4,3)