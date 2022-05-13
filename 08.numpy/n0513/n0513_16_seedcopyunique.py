import numpy as np

# 중복제거 후 출력
list1 = [1,3,4,3,1,5,7,7,9]
arr = np.array(list1)
print(arr)
# 행렬에 중복이 있을 경우 중복을 제거하고 출력
print(np.unique(arr))
print(len(np.unique(arr)))


# 값저장 주소를 다르게 하려면 copy
# 깊은 복사
# arr = np.arange(10)
# arr2 = arr.copy()
# arr2[0]=1000
# print(arr2)
# print(arr)

# 그냥 주소만 복사하는 것은 얕은 복사

# 행렬의 위치 값을 입력하면 그 값이 변경
# arr = np.arange(10)
# print(arr)
# arr[3] = 100
# print(arr)

# # 행렬 복사
# arr2 = arr
# print(arr2)

# arr2[0] = 1000
# print(arr2)

# # arr[0]방의 값도 1000으로 변경되어 있음.
# print(arr)


# 랜덤숫자를 1번만 생성후 랜덤숫자가 변경되지 않음.
# np.random.seed(7)
# arr = np.random.randint(0,10,(2,3))
# print(arr)

# arr = np.random.randint(0,10,(2,3))
# print(arr)

