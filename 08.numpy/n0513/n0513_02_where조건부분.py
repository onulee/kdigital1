import numpy as np

# where
arr = np.arange(8)
# where절에 조건만 있을시 : idx (위치값이 존재)
# 0 1 2 3 4 5 6 7
# idx = np.where(arr>5)
# print(type(idx))
# # print(arr[idx])

# 조건식만 넣으려면 where절을 사용할 필요가 없음.
idx = arr>5
print(idx)
print(arr[idx])


# where절에 조건과 결과식이 포함 :
arr2 = np.where(arr>5,100,0)
print(type(arr2))



# 1~7까지 2,2배열
# arr = np.arange(1,9).reshape(2,4)
# print(arr)

