n = int(input("Enter a number to find factors: "))
print("Factors of number {} are : ".format(n))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# output
'''
Enter a number to find factors: 10
Factors of number 10 are : 
1
2
5
10
'''