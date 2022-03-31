# 2 * 1 = 2
# 2 * 2 = 4.....

# 단 출력
for i in range(2,9): # 2,4,6,8 
    # if
    if i%2==0:
        # 1 - 9
        for j in range(1,10):
            if j%2==1:
                print('{} * {} = {}'.format(i,j, i*j))