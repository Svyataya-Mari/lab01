a = int(input("Enter number 1"))
b = int(input("Enter number 2"))
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)
gcd(a, b)