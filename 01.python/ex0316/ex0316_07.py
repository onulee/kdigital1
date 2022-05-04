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

print('[ 영어 단어 테스트 ]')
print('1. 초등1-2학년')
print('2. 초등3-4학년')
ch1 = int(input('난이도를 선택하세요>>'))

# 난이도 선택
if ch1==1:
    level=words
elif ch1==2:
    level=words2
    
wordlist=[]

for word in level:
    inwds = input('{}의 영어단어를 입력하세요.(0.프로그램종료)>>'.format(word))
    if inwds.isdigit():
        if inwds == 0:
            print('프로그램을 종료합니다.')
            break
    if words[word] == inwds:
        print('정답입니다. {} : {}'.format(word,words[word]))
        #     [입력한value, 정답, key,value]
        wlist=[inwds,'O',word,words[word]]
        wordlist.append(wlist)
    else:
        print('오답입니다. {} : {}'.format(word,words[word]))
        wlist=[inwds,'X',word,words[word]]
        wordlist.append(wlist)

# 정답, 오답 개수변수
ocount,xcount=0,0

# 정답,오답 출력
print('[ 정답확인 ]')
print('-'*50)
for idx,wlist in enumerate(wordlist):
    if 'O' in wlist:  # [입력한value, 정답, key, value]  
        ocount +=1
        print('{}.{}, {}:{}'.format(idx+1,'정답',wlist[2],wlist[0]))
    else:
        xcount +=1                  
        print('{}.{}, {}:{} 입력값:{}'.format(idx+1,'오답',wlist[2],wlist[3],wlist[0]))
# 최종개수 출력        
print('정답: {}, 오답:{}, 점수:{}점'.format(ocount,xcount,ocount*10))        
# 정답: 9 오답:1 90점
    


