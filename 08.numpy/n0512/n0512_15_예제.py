import numpy as np

# 0-7까지 1차원 행렬, (2,4)2차원 행렬로 변경하고, 
# 다시(2,2)의  3차원 행렬로 변경하시오.
arr1 = np.arange(8)
arr2 = arr1.reshape(2,4)   # 2*4=8개
# 2개 (2,2)
arr3 = arr2.reshape(2,2,2) # 8개
# 3차원 배열에서 숫자 4를 출력하시오.
print(arr3[1][0,0]) # 숫자4
# print(arr3[1,0,0]) # 숫자4
print(arr3[0][1,1]) # 숫자3
# print(arr3[0,1,1]) # 숫자3
print(arr3[1][1,0]) # 숫자6
print(arr3)


# 1부터 4까지 (2,2) 행렬을 생성하고, 2값을 출력하시오.
# * 2차원 행렬을 1차원 행렬로 변경하시오.
arr4 = np.arange(1,5).reshape(2,2)
print(arr4[0][1])
arr5 = arr4.reshape(4)
# flatten() : 1차원행렬 변경
# arr5 = arr4.flatten()
print(arr5)

# 15, 8, 12, 11, 7, 3  (2,3)행렬을 만드시오. 
# 10보다 큰수가 몇 개인지 출력하시오.
list_data = [[15,8,12],[11,7,3]]
arr6 = np.array(list_data)
print(arr6)
idx = np.where(arr6>10)
print(arr6[idx].size)
print(arr6[idx])

