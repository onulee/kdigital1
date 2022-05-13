import numpy as np

### 2차원 정렬
arr = np.array([[5,9,10,3,1],[8,3,4,2,5]])
print(arr)

# 2차원 행렬 낮은수는 위쪽, 높은수는 아래쪽으로 정렬
arr.sort(axis=0)
print(arr)


### 1차원 정렬

# # numpy정렬 : sort()
# list1 = [9,2,7,5,6,8,1,4,3,0]
# arr = np.array(list1)
# print(arr)
# # 1차원 행렬 순차정렬
# # arr.sort()
# # print(arr)

# # 1차원 행렬 역순정렬
# # 순차정렬을 한후
# arr.sort()
# # :: -1역순으로 출력
# print(arr[::-1])