data = "aaa,bbb,ccc"
data_02 = "aaa bbb ccc"
data_03 = "aaa\tbbb\tccc"
data2 = data.split(",")
print(data2)
print(type(data2))

data_02 = data_02.split(" ")
print(data_02)

data_03 = data_03.split("\t")
print(data_03)
