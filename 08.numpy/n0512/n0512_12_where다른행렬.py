import numpy as np

arr1 = np.array([
    [10,20,30],
    [3,50,5]
])

arr2 = np.array([
    [70,80,90],
    [100,110,120]
])

# where
print(arr1)
arr3 = np.where(arr1>20,arr1,arr2)
print(arr3)






