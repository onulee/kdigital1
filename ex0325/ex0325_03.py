from stumanage.student import Student

# 클래스의 생성자를 최초 호출
s1 = Student('홍길동')
s2 = Student('홍길동',90,90)

print(s1)
print(s2)
if s1==s2:  #주소값 == 주소값
    print('같습니다.')
else:
    print('주소가 다릅니다.')    