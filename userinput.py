name = input("whats your name: ")
print("Hello " + name)
height = float(input("whats your height: "))
height_inches = "{:.2f}".format(height/2.54)
print("You are " + str(height) + "cm")
print("you are " + height_inches + " inchesTall")