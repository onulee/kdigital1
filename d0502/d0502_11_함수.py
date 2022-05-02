import pandas as pd

def add_cm(height):
    height = str(height)+'cm'
    return height

def capChange(word):
    # pandas null 인지 아닌지 확인
    if pd.notnull(word):
        word = word.capitalize()
    return word

def lowerChange(word):
    word = word.lower()
    return word

def tranWord(height):
    # 188이상이면 cm, 188미만 센티미터
    if height >=188:
        height = str(height)+'cm'
    else:
        height = str(height)+'센티미터' 
    return height


df = pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

# 형변환후 더하기 실행
# df['키'] = df['키'].astype(str) + 'cm'

# 함수적용 apply() 호출
# df['키'] = df['키'].apply(add_cm)
# print(df)

# 함수적용 capChange()함수 호출
# nan데이터 처리
# df.fillna('java',inplace=True)
# df['SW특기'] = df['SW특기'].apply(capChange)

# 188이상이면 cm, 188미만 센티미터
df['키'] = df['키'].apply(tranWord)


print(df)