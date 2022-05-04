from random import *
words = {
    "자동차":'car',
    '의자':'chair',
    '사랑':'love',
    '국수':'noodle',
    '돼지':'pig',
    '호랑이':'tiger',
    '직업':'job',
    '사과':'apple',
    '사자':'lion',
    '여우':'fox'
}

# 랜덤으로 5개를 뽑는다.
level1 = list(words.keys())
rantemp=[]
count=0
while count<5:
    rno = randint(0,8)
    if not level1[rno] in rantemp:
       rantemp.append(level1[rno])
    else:
        continue
    count += 1
print(rantemp)    