'''
Python program to solve quadratic equation
Quadratic equation:

Quadratic equation is made from a Latin term "quadrates" which means square. It is a special type of equation having the form of:

ax2+bx+c=0
Here, "x" is unknown which you have to find and "a", "b", "c" specifies the numbers such that "a" is not equal to 0. 
If a = 0 then the equation becomes liner not quadratic anymore.

In the equation, a, b and c are called coefficients.
'''

import math
a = int(input())
b = int(input())
c = int(input())

if(a==0):
    print("Invalid Input")
else:
    val = (b**2) - (4*a*c)
    root = math.sqrt(abs(val))
    if(val>0):
        print("Two Real Roots")
        print((-b + root)/(2*a))
        print((-b - root)/(2*a))
    elif(val==0):
        print("One Real Root")
        print(-b/(2*a))
    else:
        print("No Real Root")
        print(-b/(2*a)," + i",root)
        print(-b/(2*a)," - i",root)
