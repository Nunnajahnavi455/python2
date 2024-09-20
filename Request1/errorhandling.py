try:
    a=int(input("enter first no:"))
    b=int(input("enter second no:"))
    print(a/b)
except ZeroDivisionError as e:
    print('cannot divide zero')
except ValueError as e:
    print("cannot convert string to int")