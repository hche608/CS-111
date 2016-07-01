#Author: Hao CHEN
#Date: May 2014

userInput = input("Please enter your name:")
print("Hello",userInput,"welcome to the ounces to millilitres converter.")

print()
userInput = float(input("Please enter a volume in ounces:"))
conversionFactor = userInput * 29.5735
print(userInput,"ounces is equivalent to",conversionFactor,"millilitres.")
