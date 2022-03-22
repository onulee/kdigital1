from tempfile import strInput,strFileSave
content=[]
str1=''

# 파일이름,파일내용을 입력받는 함수
str1 = strInput(str1,content)

# 파일저장 함수
strFileSave(str1,content)

    
    




# if '1.txt' in os.listdir():
#     print('있습니다.')
#     with open('1.txt','a',encoding='utf-8') as file:
#         file.write('파일을 추가해서 저장시킵니다.\n')
# else:
#     print('없습니다.') 
#     with open('1.txt','w',encoding='utf-8') as file:
#         file.write('파일을 새로만들어서 저장시킵니다..\n')   