import json
data = json.load(open('stuData.json','r')) 
print(data[-1]['stuno']+1)