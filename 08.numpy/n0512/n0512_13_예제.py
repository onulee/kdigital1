import numpy as np

# 1부터 100사이의 랜덤수를 넣어서, (10,10)행렬을 생성하시오.
# 위 행렬에서 50이상인 값을 출력하시오.
arr = np.random.randint(1,100,(10,10))
print(arr)
idx = np.where(arr>=50)
print(arr[idx])
print(arr[idx].size)

print(arr.shape)
print(arr.size)

# 0부터 20 사이 랜덤수를 넣어서, 10보다 크면 그대로,
# 10보다 작으면 0을 입력하시오.
arr2 = np.random.randint(0,20,20)
idx2 = np.where(arr2>10,arr2,0)
print(arr2[idx2])
print(arr2[idx2].size)
print(idx2.size)



# arr = np.random.randint(1,100,(10,10))
# print(arr)
# idx = np.where(arr>=50)
# print(arr[idx])


# arr2 = np.random.randint(0,20,20)
# idx = np.where(arr2>10,arr2,0)
# print(arr2[idx])
