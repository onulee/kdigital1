import os
print(os.listdir())
# 1. 파일이름을 1.txt 
# 2. 내용은 "파일이름저장완료" 글자를 저장
# 3. 파일을 저장
# 조건 : 동일한 파일이름이 있으면
# 파일이름을 1_1.txt 변경해서 저장시키시오.
# 동일한 파일이름이 없으면 1.txt 저장시키시오.

str1='1.txt'




# if '1.txt' in os.listdir():
#     print('있습니다.')
#     with open('1.txt','a',encoding='utf-8') as file:
#         file.write('파일을 추가해서 저장시킵니다.\n')
# else:
#     print('없습니다.') 
#     with open('1.txt','w',encoding='utf-8') as file:
#         file.write('파일을 새로만들어서 저장시킵니다..\n')   