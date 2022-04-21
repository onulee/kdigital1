import re



rate ="후기평점 4.8점"
# sub()함수는 string에서 pattern과 일치하는 문자들을 지정하는형태로 교체
# re.sub(r'[패턴-정규표현식]','해당부분을 교체할 내용',rate)
# re.sub()안에 ^ not을 의미함.
re_rate = re.sub(r'[^0-9.]','',rate)
print(re_rate)


# text="123abc456"
# re_text = re.sub(r'[^0-9]','',text)
# print(re_text)

# re.compile("[0-9]")
# rate = rate[5:8]
# print("평점 : ",rate)

