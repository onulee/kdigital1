import json
stuSave =[
    {'stuno': 1, 'stuname': '홍길동', 'kor': 100, 'eng': 100, 'total': 200, 
'avg': 100.0, 'rank': 0}
]

#json파일 저장함수
json.dump(stuSave,open('3.json','w'))
print(stuSave)

#json파일 읽어오기
data2 = json.load(open('3.json'))
print(data2)