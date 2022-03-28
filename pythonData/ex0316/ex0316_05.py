import operator

tdic,tlist={},[]
tdic={'love':'사랑','chair':'의자','game':'게임','car':'자동차'}
# key와 value를 튜플형태로 출력 - list형태로 출력
tlist2 = list(tdic.items())
tlist2.sort(reverse=True)
print(tlist2)
tlist = sorted(tdic.items(),key=operator.itemgetter(-1))
# print(tlist)
# print(tdic.keys())
# print(list(tdic.keys()))
# print(tdic.values())


# tlist=[4,6,1,8,9,11,2]
# 기존list는 변경되지 않고 새로운 리스트에 복사
# tlist2 = sorted(tlist)
# print(tlist2)
# print(tlist)
# # tlist.sort(reverse=True)
# # print(tlist)
# tlist.reverse()
# print(tlist)
