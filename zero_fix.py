a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))


def div():
    if b == 0:
        t = "Can't divide by zero!"
        return t
    r = a / b
    return r