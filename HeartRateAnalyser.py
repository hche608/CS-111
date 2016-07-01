#Author: Hao CHEN
#Date: May 2014

print("This program will analyse your resting heart rate.")
userInput = int(input("Please enter your resting heart rate:"))
print("You have a resting heart rate of",userInput,"bpm.")
if userInput < 60 :
    print("Your may have bradycardia.")
elif userInput < 101 :
    print("Your resting heart rate is normal.")
else :
    print("You may have tachycardia.")
