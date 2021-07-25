#Program to check whether a given number is a prime number or not. The given number N, a positive integer, will be passed to the program using the first command line parameter. If it is a prime number the output should be the square root of the number up to 2 decimal point precision, If it is not a prime number then print 0.00 to stdout
import math
n = int(input().strip())
if(n<=0):
    print("enter positive number:")
elif(n>0):
    if(n>1):
       for i in range(2, n//2):
        if (n % i) == 0:
            print("0.00")
            break
        else:
            print("{:2f}".format(math.sqrt(n)))
            break
            
