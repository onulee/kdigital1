# 1-25까지 list만들어보세요.
arrs = [i for i in range(1,26)]

for arr in arrs:
    print('{:2d}'.format(arr),end=' ')
    if arr%5 == 0:
        print()
