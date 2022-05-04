# 주민번호 뒤자리를 입력받아 남자,여자를 출력하시오.
# 7자리가 아니면 다시 입력받음.
# 990101-1105555
# 1,3 - 남자 2,4-여자 다시입력받음.
while True:
    # 입력한 데이터 : str타입
    inNum = input('주민번호 뒤 7자리를 입력하세요.')
    if len(inNum) != 7:
        print('7자리가 아닙니다. 다시 입력하세요.!!')
        continue
    temp = inNum[0]
    if temp=='1' or temp=='3':
        print('남자입니다.')
        break
    elif temp=='2' or temp =='4':
        print('여자입니다.')
        break
    else:
        print('잘못입력하셨습니다.!!')
        continue
    




# 문자열 슬라이싱
# str1 = '안녕하세요. 파이썬입니다.'
# print(str1[7:])
# print(str1[2])



# str - len()함수
# alist = [123,46,3451,484,1,50,111,33333,9,1000000]
# numlist=['짝수','홀수']
# # 123[3자리]:홀수
# # 46[2자리]:홀수
# for i in alist:
#     print('{}[{}자리]:{}'.format(i,len(str(i)),numlist[i%2]))


# a='안녕하세요. 파이썬수업에 오신것을 환영합니다.'
# alist = [1,2,3,4,5]
# print(alist[2])
# print(a[2])

# print(len(alist))
# print(len(a))