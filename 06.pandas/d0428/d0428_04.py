import pandas as pd
# 시각화 라이브러리 - 그래프
import matplotlib.pyplot as plt
import matplotlib

# data : dic타입
data = {
'이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
'학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
'키' : [197, 184, 168, 187, 188, 202, 188, 190],
'국어' : [90, 40, 80, 40, 15, 80, 55, 100],
'영어' : [85, 35, 75, 60, 20, 100, 65, 85],
'수학' : [100, 50, 70, 70, 10, 95, 45, 90],
'과학' : [95, 55, 80, 75, 35, 85, 40, 95],
'사회' : [85, 25, 75, 80, 10, 80, 35, 95],
'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

# data를 pandas DataFrame 2차원데이터로 변환
# df = pd.DataFrame(data)
# 2차원 배열형태 구성
# print(df)

# index 추가해서 DataFrame 변환
df = pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
print(df)
print(type(df))
# index만 출력
print(df.index)


# index.name : 이름지정, set_index : 추가, reset_index : 삭제

# index이름 지정
df.index.name = '지원번호'
print(df)

# index지정만 삭제가 되고, index지정된 컬럼은 존재
# df.reset_index(inplace=True)
# print(df)

# index지정된 컬럼까지 삭제 - drop=True
df.reset_index(drop=True,inplace=True)
# print(df)

# 이름을 index로 지정
df.set_index('이름',inplace=True)
# print(df)

# index 순차정렬
df.sort_index(inplace=True)
print(df)

# index 역순정렬 (ascending=False)
df.sort_index(ascending=False,inplace=True)
print(df)

# matplotlib 그래프 생성
# x= data['이름']
# y = data['국어']
# plt.plot(x,y)
# plt.title('국어성적')
# plt.show()