#!/usr/bin/python3

def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    larger, smaller = 0, 0
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)

    if a > b:
        print("{} is greater than {}".format(a,b))
    elif a < b:
        print("{} is greater than {}".format(b,a))
    else:
        print("{} and {} are equal".format(a,b))
    list = []
    list[:] = range(100)
    if a in list and b in list:
        print("Both numbers are between 0 and 100")
    elif a in list and b not in list:
        print("{} is between 0 and 100, but {} is not".format(a,b))
    elif a not in list and b in list:
        print("{} is between 0 and 100, but {} is not".format(b,a))
    else:
        print("The numbers are outside the range.")
if __name__ == "__main__": main()