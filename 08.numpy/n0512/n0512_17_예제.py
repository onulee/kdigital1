import numpy as np

# # (3,5)행렬 : 1로 채우기
# arr1 = np.zeros([3,5])
# arr1 = np.ones([3,5])
arr1 = np.full([3,5],7)
print(arr1)


# # (3,2)행렬 : 랜덤 1,10숫자를 채우기
# arr2 = np.random.randint(1,10,(3,2))
# 16-11+1=6개
arr2 = np.arange(0,11,2).reshape(3,2)
# arr2 = np.arange(0,10).reshape(2,5)
print(arr2)

# # 열기준으로 행렬 합치기 
arr3 = np.concatenate([arr1,arr2],axis=1)
# arr3 = np.concatenate([arr1,arr2],axis=0)
print(arr3)

# 열기준으로 (3,4)(3,3) 행렬나누기
left,right = np.split(arr3,[4],axis=1)
print(left)
print(right)

# 행기준으로 (2,7)(1,7) 행렬나누기
top,bottom = np.split(arr3,[2],axis=0)
print(top)
print(bottom)
