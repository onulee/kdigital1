import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# list
list_data = [1,2,3]
print(list_data)
# list 0주소 출력
print(list_data[0])

# list타입에 3을 더하는 것은 불가능 : list_data+3
# list 모든 list에 3을 더함.
# for i in range(len(list_data)):
#     list_data[i] = list_data[i]+3
# print(list_data)

# numpy형태로 변경
arr = np.array(list_data)
print(arr)
print(arr[0])
# 모든 행렬에 3을 더함
print(arr+3)

# numpy배열 크기
print(arr.shape)
# numpy배열 크기
print(arr.size)
# numpy 타입
print(arr.dtype)