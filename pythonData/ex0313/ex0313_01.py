arr_list = [
    [1,2,3,4,5],
    [6,7],
    [8,9,10]
]

for arr in arr_list:
    for i in arr:
        print(i)



# arr_list = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

# # 2차원 리스트는 for를 2번 돌려야 함.
# for arr in arr_list:
#     for i in arr:
#         print(i)



# arr_list = [1,2,3,4,5,6,7]
# for arr in arr_list:
#     print(arr)


# 2개의 입력한 숫자의 사이의 합을 출력하시오.
# 타입 : bool-True/False, int-정수형, float-실수형, str-문자열
# 나누기-> int:float, 더하기,빼기,곱하기->int
# start = int(input('숫자1을 입력하세요.>>'))
# end = int(input('숫자2를 입력하세요.>>'))

# if end<start:
#     start,end = end,start

# total = 0
# for i in range(start,end+1):
#     total += i
# print('합 :{}'.format(total))    





# total=0
# for i in range(1,101):
#     total += i
    
# print('1부터 100까지의 합 : ',total)    