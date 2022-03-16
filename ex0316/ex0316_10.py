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
words2 = {
    '연필':'pencil',
    '자':'ruler',
    '책':'book',
    '양말':'sock',
    '모자':'hat',
    '개':'dog',
    '잠':'sleep',
    '먹다':'eat',
    '읽다':'read',
    '피아노':'piano',
}

from random import *
# tdic ={ key:value } 10개를 출력하시오.

# 타입 : list
ww = list(words.keys())
wwv = list(words.values())
wlist = list(words.items())
count=0

# print(wlist[0][0])

listtemp=[] # 임시저장list
while count<5:
    rno = randint(0,9)
    # 랜덤으로 리스트에 담기
    # [("자동차":'car')] 튜플 형태로 비교 가능
    if not wlist[rno] in listtemp: 
        listtemp.append(wlist[rno])
        count +=1
        
print(listtemp)        
    

