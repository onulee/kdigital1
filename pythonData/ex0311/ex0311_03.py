score = int(input('점수를 입력하세요.>>'))
msg=''  # 전역변수

# 한줄 if문
# msg='합격' if score>=60 else '불합격'

# if문
if score>=60:
    msg = '합격'
else:
    msg = '불합격'    
    
print(msg)    