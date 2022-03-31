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

# totallist=[키] words 5개, words2 5개 랜덤 keys으로 담아보세요.
# totallist 10개의 개수를 출력하시오.

#### 추가옵션.1
# 튜플 리스트
wtuple = list(words.items())
print(wtuple)
print(wtuple[0])
# 튜플 -> 딕셔너리로 변환
wdic = dict(wtuple)
print(type(wdic))
print(wdic)
# tdic ={ key:value } 10개를 출력하시오.

#### 추가옵션.2
# words, words2 의 개수를 입력받아 딕셔너리에 담아보세요.
# 예) words 3개, words2 7개