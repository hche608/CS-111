#Author: Hao CHEN
#Date: May 2014

#Define the value of our variables
squaresInBlock = 48
numberOfBlocks = 5
numberOfPeople = 13

#Calculate the results
totalSquares = squaresInBlock * numberOfBlocks
eachPerson = totalSquares // numberOfPeople
leftOver = totalSquares % numberOfPeople


#Display the output
print("There are",totalSquares,"squares in",numberOfBlocks,"blocks of choclate.")
print("Each person receives",eachPerson,"squares of choclate.")
print("There are",leftOver,"squares of choclate left over.")
