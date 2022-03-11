import datetime

# 현재시간을 가져옴.
now = datetime.datetime.now()
month1 = now.month

# 3,4,5 -> 봄입니다.
if 3 <= month1 <=5:
    print('봄입니다.')
# if now.month == 3 or now.month == 4 or now.month == 5:
# if (now.month == 3 or 4 or 5): # (X) now.month 숫자인지 아닌지 
elif 6<= now.month <=8:
    print('여름입니다.')
# 6,7,8 -> 여름입니다.
elif 9<= now.month <=11:
    print('가을입니다.')
# 9,10,11 -> 가을입니다.
elif now.month==12 or now.month==1 or now.month==2:
# else:    
    print('겨울입니다.')
# 12,1,2 -> 겨울입니다.



# print(now)
# # 현재년도,월,일,시,분,초
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)