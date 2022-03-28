str1 = 'PYTHON Is Easy'
print(str1.startswith('P')) #시작부분 확인
print(str1.endswith('z'))   #끝부분 확인

# 대소문자가 구분없이 PYthon
# in_str = input('문자를 입력하세요.>>')
# if in_str.lower() in str1.lower():
#     print('{}는 존재합니다.'.format(in_str))
# else:
#     print('{}은 글자가 없습니다.'.format(in_str))    



# print(str1.count('python')) #똑같은 글자가 몇개인지 알려줌.
# print(str1.find('t'))
# print(str1.find('as'))
# print(str1.index('t'))
# if 'th' in str1:
#     print(str1.index('th'))
# else:
#     print('없습니다.')    



# print(str1.upper()) #대문자
# print(str1.lower()) #소문자
# print(str1.swapcase()) #대문자->소문자, 소문자->대문자
# print(str1.title())    #첫글자 대문자로
# print(str1.isupper())  #첫글자가 대문자인지 확인



# list1 = [10,4,3,9,20,21]
# list2 = [21,20,9,3,4,10] #역순출력
# list3 = [3,4,9,10,20,21] #순차정렬
# list4 = [21,20,10,9,4,3] #역순정렬

# list1.reverse()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# inStr='서울인재개발원'

# inStr,outStr='',''
# count,i=0,0

# inStr = input('원하는 글자를 입력하세요.>>')
# count = len(inStr) # 7

# for i in range(0,count):
#     outStr += inStr[(count-1)-i]   

# print(outStr)    
    


# str1 = '서울인재개발원 파이썬수업'
# for i in range(len(str1)):
#     if i==0:
#        print(str1[i],end='')
#     else:
#        print(','+str1[i],end='')
    