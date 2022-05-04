# 1-25까지 list만들어보세요.
# [
#   [1,2,3,4,5],
#   [6,7,8,9,10]  
#]

# 1,25까지의 리스트를 생성
arrs = [i for i in range(1,26)]
# 2차원 리스트 생성
# arrs2 = [{},{},{}]
arrs2 = [[],[],[],[],[]]
# [1,2,3,4,5.....]
# i = 0,1,2,3,4,5,......
for i,arr in enumerate(arrs):
    arrs2[i//5].append(arr)
    
print(arrs2)  
print("[0][0] 데이터 :",arrs2[0][0])  
print("[1][0] 데이터 :",arrs2[1][0])  
print("[2][2] 데이터 :",arrs2[2][2])  
