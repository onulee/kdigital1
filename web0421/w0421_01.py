import re



rate ="후기평점 4.8점"
# sub()함수는 string에서 pattern과 일치하는 문자들을 지정하는형태로 교체
# re.sub(r'[패턴-정규표현식]','해당부분을 교체할 내용',rate)
# re.sub()안에 ^ not을 의미함.
# re_rate = re.sub(r'[^0-9.]','',rate)
# print(re_rate)

# 정규표현식 [0-9a-zA-Z]안에 해당되는 것은 교체
text="123aabcA456**&ass"
re_text = re.sub(r'[\d]','',text)

print(re_text)

# re.compile("[0-9]")
# rate = rate[5:8]
# print("평점 : ",rate)

