#import math lib
import math
#take user inputs
N = int(input('Enter the number of students :'))
R = int(input('Enter the number of seats :'))
#factorial by using factorial() function
nume = math.factorial(N)
deno = math.factorial(N-R)
#permutation = n! / (n-r)!
no_of_ways = nume//deno
#print total no of ways
print('Total number of ways are :' + str(no_of_ways))
