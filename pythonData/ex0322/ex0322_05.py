import os

# 파일쓰기
# with open('1.txt','w',encoding='utf-8') as file:
#     file.write('aaa')

# 파일내용추가
# with open('1.txt','a',encoding='utf-8') as file:
#     file.write('6\t김유신\t100\t100\t200\t100.0\t0\n')

# 파일읽어오기    
# with open('1.txt','r',encoding='utf-8') as file:
#     print(file.read())
    
with open('1.txt','r',encoding='utf-8') as file:
      lines = file.readlines()
      for line in lines:
          print(line,end='')  
          
          
os.remove('1.txt')          
          
    
# 파일의 내용을 1줄씩 읽어와서 출력    
# with open('1.txt','r',encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:  
#             break
#         print(line,end='')