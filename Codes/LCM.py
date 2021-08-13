import math

def find_lcm(a,b):
    temp = math.gcd(a,b)
    result = (a*b)/temp
    return result

a = int(input())
b = int(input())

print(find_lcm(a,b))
