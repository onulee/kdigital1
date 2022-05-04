import pandas as pd

df=pd.read_excel('user.xlsx')

# .com으로 끝나는 email컬럼 출력
filt = df['email'].str.endswith('.com')
# print(filt)
# print(df[filt]) #filt = True,False
# print(df[filt]['email']) #filt = True,False

# email컬럼에서 3번째 자리에 a가 있는 이메일 출력 : 237개
filt = df['email'].str.find('a',2)
print(filt)  # True,False
print(df[filt==2])

#isin 뒤에는 list타입이어야 가능, []타입변경
filt = df['email'].str[2].isin(['a'])
print(df[filt])


