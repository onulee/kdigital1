# a = 1
# b = 2
# c = a
# print(a)
# print(b)
# print(c)

# a = 2
# print(a) #2
# print(c) #1

a = [1]
b = [2]
c = a  # 주소가 복사가 되는 것임.

print(a) #1
print(b) #2
print(c) #1

a[0] = 10
print(a)   # 10
print(c)   # 10

