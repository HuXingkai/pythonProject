# file=open("test.txt")
# data=file.read()
# print(data)
# file.close()

with open("test.txt") as file:
    data=file.read()
    print(data)
