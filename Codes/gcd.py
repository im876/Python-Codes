#Write a program, to find the GCD of the given 2 numbers, using command line arguments. The input is 2 integer and the output GCD also should be an integer value.

import math
a,b = map(int, input().strip().split())
print(math.gcd(a,b))
