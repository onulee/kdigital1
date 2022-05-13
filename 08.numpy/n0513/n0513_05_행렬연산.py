import numpy as np

# 랜덤으로 1,10사이 행렬을 만들고, (2,2)행렬로 변경
# 행렬 곱하기
# arr = np.random.randint(1,10,4).reshape(2,2)
# print(arr)
# arr = arr*10
# print(arr)

# # where절을 사용하여 행렬 곱셈연산
# arr2 = np.random.randint(1,10,25).reshape(5,5)
# print(arr2)
# arr3 = np.where(arr2>5,arr2*10,arr2)
# print(arr3)




### 행렬끼리 빼기 연산
# arr = np.array([20,30,40,50])
# arr2 = np.arange(4)
# # 2개의 행렬 빼기 연산
# arr3 = arr-arr2
# print(arr)
# print(arr2)
# print(arr3)





# list_data = [1,3,5,7,9,11]

# # ### numpy 행렬 전체적으로 더하기 연산
# arr = np.array(list_data)
# print(arr)
# arr2 = arr+3
# print(arr2)

# numpy 행렬 빼기
# arr2 = arr-4
# print(arr2)





### list데이터에 바로 더하기를 할수 없음.
# list에 3을 더함
# list_data2 = list_data + 3 # error
# print(list_data2)


### list데이터에 더하기 연산
# # list타입에 전체적으로 3을 더함.
# list_data2=[]
# print(list_data)
# for i in list_data:
#     list_data2.append(i+3)
    
# print(list_data2)    