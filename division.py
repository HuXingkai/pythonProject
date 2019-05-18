print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first=input('\nFirst number')
    if first=='q':
        break
    second=input('Second number')
    if second=='q':
        break

    try:
        answer=float(first)/float(second)

    except ZeroDivisionError:
        print('不能除以0')
    else:
        print(answer)