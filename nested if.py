#nested if
#check if the given num is a three digit even number
num = int(input("Enter a num :"))
if num > 99 and num < 1000:
    if num % 2 == 0:
        print(num, "is a three digit even number")
    else:
        print(num, "is not a three digit even number")


