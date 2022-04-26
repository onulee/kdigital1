img_item = 'background-image: url("https://yaimg.yanolja.com/v5/2018/07/19/16/1280/5b5044af556398.30978172.jpg");'

# https 시작하는 위치 값을 가져옴.
temp = img_item.find("https")
print(temp)
img_item = img_item[temp:-3]
print("파일 위치 : ",img_item)

