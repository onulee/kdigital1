import json
data =[
    {'stuno':1,'stuname':'홍길동','kor':100,'eng':100,\
            'total':200,'avg':(200)/2,'rank':0},
    {'stuno':2,'stuname':'이순신','kor':100,'eng':100,\
            'total':200,'avg':(200)/2,'rank':0}
]

#json파일 저장함수
json.dump(data,open('2.json','w',encoding='utf-8'))

#json파일 읽어오기
data2 = json.load(open('2.json',encoding='utf-8'))
print(data2)