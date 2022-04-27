import smtplib
from email.mime.text import MIMEText

# gmail이메일서버 사용방법
# naver동일
# google계정관리 > 보안 클릭
# password 2단계인증 사용 -> 앱 비밀번호 16자리 사용
# ( 토큰키 생성후 사용하면 발송됨.)
# smtp.gmail.com:587

# smtp서버명
smtpName = "smtp.gmail.com"
smtpPort = 587

sendEmail = "onulee74@gmail.com"
password="16자리"  #앱비밀번호 넣어야 함.
recvEmail = "onulee74@gmail.com" #받는사람주소

#글자
title="gmail발송제목"
content = "gmail 발송내용입니다."

#MIME객체
msg = MIMEText(content)
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subject'] = title

# 메일서버 정보
s = smtplib.SMTP(smtpName,smtpPort)
s.starttls() # 서버접근
s.login(sendEmail,password) #서버로그인
# 메일 발송(보내는주소,받는주소,내용)
s.sendmail(sendEmail,recvEmail,msg.as_string())

s.close()