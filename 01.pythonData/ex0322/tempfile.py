import os
# 파일저장 함수
def strFileSave(str1,content):
    if str1 in os.listdir():
        # aaa_1.txt
        str1 = str1[:str1.find('.')]+'_1'+str1[str1.find('.'):]
        with open(str1,'w',encoding='utf-8') as file:
            for i in range(len(content)):
                file.write(content[i])
    else:
        with open(str1,'w',encoding='utf-8') as file:
            for i in range(len(content)):
                file.write(content[i])   



# 파일이름,파일내용을 입력받는 함수
def strInput(str1,content):
    str1=input('파일이름을 입력하세요.(확장자명은 자동으로 입력됨)')   # aaa_1.txt  
    str1 = str1+'.txt'

    print('[ 아래에 저장할 내용을 입력하세요. 파일명 :{} ]'.format(str1))
    count=1
    while True:
        temp = input('{}줄 :'.format(count))
        if temp=='0':
            break
        content.append(temp+'\n')
        count += 1
        
    return str1    