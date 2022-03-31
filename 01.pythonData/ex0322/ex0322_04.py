import os

with open('1.txt','w',encoding='utf-8') as file:
    file.write('1\t홍길동\t100\t100\t200\t100.0\t0\n')
    file.write('2\t이순신\t100\t100\t200\t100.0\t0\n')
    file.write('3\t유관순\t100\t100\t200\t100.0\t0\n')
    file.write('4\t강감찬\t100\t100\t200\t100.0\t0\n')
    file.write('5\t김구\t100\t100\t200\t100.0\t0\n')


# file = open('1.txt','w',encoding='utf8')
# file.write('글을 다른형태로 쓰기합니다.\n')
# file.close()  # open받는 file에서는 꼭 close()해야 함.

# with open('1.txt','w',encoding='utf-8') as file: #w 덮어쓰기, a 추가
#     file.write('파이썬수업이 진행중입니다.\n')
#     file.write('현재 모듈수업입니다.\n')
#     file.write('file저장입니다.\n')
    
# with open('1.txt','a',encoding='utf-8') as file:
#     file.write('다시 글을 입력합니다.\n')    


# print(os.name)
# print(os.getcwd())  #현재위치
# print(os.listdir()) #현재 폴더안에 무슨폴더가 있는지 출력

# os.mkdir('py')  # 폴더생성함수
# os.rmdir('py')    # 폴더삭제함수

