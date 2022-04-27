# 메일발송 라이브러리
import smtplib
from email.mime.text import MIMEText

smtpName = "smtp.naver.com" # 메일서버주소
smtpPort = 587              # 메일서버 포트번호

sendEmail="onulee@naver.com"  # 자신의 아이디
password="1111"               # 자신의 패스워드
recvEmail="onulee@naver.com"  # 받는사람 주소

# 글쓰기 제목,내용
title="파이썬 이메일 보내기 수업"
content ="파이썬 수업이 진행중입니다. 현재 38일차입니다."

# MIME 객체
msg = MIMEText(content)
msg['From']=sendEmail
msg['To']=recvEmail
msg['Subject']=title

# 메일서버주소 정보 smtp.naver.com/587
s = smtplib.SMTP(smtpName,smtpPort)
# 메일 서버 접근
s.starttls()
# 메일 서버 로그인(id,pw입력)
s.login(sendEmail,password)
# 메일 발송(보내는주소, 받는주소, 내용)
s.sendmail(sendEmail,recvEmail,msg.as_string())
# 메일 닫기
s.close()