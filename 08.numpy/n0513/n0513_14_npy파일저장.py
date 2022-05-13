import numpy as np

# npy파일 저장
# np.save - 저장
# np.load - 읽어오기

### npy 2개이상 저장
arr1 = np.arange(10)
arr2 = np.arange(10,20)

# 2개이상 array저장 savez저장, npz파일명
# a1:key, arr1:values
np.savez('np2.npz',a1=arr1,a2=arr2)

# 2개이상 파일 읽어오기
r_arr = np.load('np2.npz')
# a1의 key값으로 호출
result1 = r_arr['a1']
print(result1)
result2 = r_arr['a2']
print(result2)




### npy파일 1개 저장방법

# # npy파일 저장
# arr = np.arange(10)
# np.save('np1.npy',arr)

# # npy파일 읽기
# read_arr = np.load('np1.npy')
# print(read_arr)