import numpy as np

### 단위행렬 연산 : 행과 열의 곱을 의미

# 0-5까지 (3,2)행렬
# 10-15까지 (2,3)행렬
# 2개의 단위행렬 연산을 하시오.
# arr1 = np.arange(6).reshape(3,2)
# arr2 = np.arange(10,16).reshape(2,3)
# # (3,3) 행렬
# arr3 = np.dot(arr1,arr2)
# print(arr3)


# randint : 1-10 15개 생성 (5,3)행렬로 변경
# [4,2,1] 1차원행렬을 생성
# 2개의 단위행렬 연산을 하시오.

# arr1 = np.random.randint(1,10,(5,3))
# print(arr1)
# arr2 = np.array([4,2,1])
# print(arr2)
# arr3 = np.dot(arr1,arr2)
# print(arr3)
 


# ## (2,2)행렬 (1,2)행렬 dot연산
# ## 연산 결과 : (1,2)행렬
# arr1 = np.array([[1,3],[2,4]])  #(2,2)
# arr2 = np.array([2,5])          #(1,2)
# result_arr =  np.dot(arr1,arr2)
# print(arr1)
# print(arr2)
# # 1*2+3*5=17, 2*2+4*5=24  [17,24]
# print(result_arr)

## (2,2)행렬 (2,2)행렬 dot연산
## 연산 결과 : (2,2)행렬


# list1 = [[1,2],[3,4]]
# list2 = [[5,6],[7,8]]

# arr1 = np.array(list1) 
# arr2 = np.array(list2)

# #  단위행렬 곱 : dot함수
# arr3 = np.dot(arr1,arr2)
# print(arr3)


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