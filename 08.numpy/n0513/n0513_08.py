import numpy as np

list1 = [[1,2],[3,4]]
list2 = [[5,6],[7,8]]

arr1 = np.array(list1) 
arr2 = np.array(list2)

#  단위행렬 곱 : dot함수
arr3 = np.dot(arr1,arr2)

print(arr3)


## numpy행렬 사칙연산
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# # 더하기
# arr3 = arr1+arr2
# print(arr3)

# # 빼기
# arr4 = arr1-arr2
# print(arr4)

# # 곱하기
# arr5 = arr1*arr2
# print(arr5)

# # 나누기
# arr6 = arr1/arr2
# print(arr6)