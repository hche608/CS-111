#Author: Hao CHEN
#Date: May 2014

n = 0
end = 10
factorial = 1
while n <= end:
    if n == 0:
        print(n,"! = ",factorial)
    else :
        factorial = factorial * n
        print(n,"! = ",factorial)
    n = n + 1
print("The end")
