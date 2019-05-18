def print_two(*args): # "*" That tells Python to take all the arguments to the function and then put
#them in args as a list.
    arg1, arg2, arg3 = args
    print(f"arg1:{arg1}, arg2:{arg2}, arg3:{arg3}")

print_two('one','two','three')
