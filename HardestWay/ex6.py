types_of_people = 10
x=f"there are {types_of_people} types of prople"
binary = "binary"
do_not = "dont`t"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f'I said {x}')
print(f'I also said: {y}')

halarious = False
joke = "Isn`t that joke so funny? {}"
#调用了字符串的.format()方法，格式化字符串，其中字符串中，需要被替换的地方用“{}”
#标识出来，其真正的字符串，通过.format()中形参传入
print(joke.format(halarious))
