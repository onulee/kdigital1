arrlist = [i for i in range(10)]
print(arrlist)
print(arrlist[6])

# arrlist[0]+arrlist[1]+arrlist[2]......+arrlist[9]

total=0
for i in arrlist:
    total += i
    print(i,end=' ')
    
print()
print('총합 :',total)    




# a,b,c,d,e,f,g,h,i,j,k=0,0,0,0,0,0,0,0,0,0
# a=0

# a=[0,0,0,0]

# arr = [0 for i in range(4)]
# arr[0]=1
# arr[1]=2
# arr[2]=3
# arr[3]=4
# total = arr[0]+arr[1]+arr[2]+arr[3]
# print(total)