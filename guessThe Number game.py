import random
num = random.randint(1,20)
print(num)
guess = int(input("Guess a number between 1 and 20: "))
attepts = 0
while num != guess and attepts < 2:
    if guess > num:
        print("Your guess is too high")
        attepts += 1


    else:
        print("Your guess is too low")
        attepts += 1

    guess = int(input("Guess again: "))

if guess == num:
    print("You won")
