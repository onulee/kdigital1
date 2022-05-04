import pandas as pd

temp = pd.Series([-20,-10,10,20],index=['Jan','Feb','Mar','Apr'])
# print(temp)
# print(temp[0])    # index번호로 출력
print(temp['Jan'])  # index 이름으로 출력