import datetime
now = datetime.datetime.now()
year = now.year
month = now.month+1
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print('{}-{}-{} {}:{}:{}'.format(year,month,day,hour,minute,second))
print(now)


# print(dir(datetime)) # 모듈에 있는 라이브러리함수를 확인

# stuSave=[]
# stuname = input('이름을 입력하세요.>>')
# now = datetime.datetime.now()
# temp={'stuname':stuname,'inputTime':'{}-{:02d}-{}'.format(now.year,now.month,now.day)}
# stuSave.append(temp)
# print(stuSave)