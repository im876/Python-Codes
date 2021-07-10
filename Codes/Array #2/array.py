import math

A =list(map(int, input().split(',')))

result = A[0]

for i in range(1, len(A)):
    result = math.gcd(result,A[i])
    print(result)
    
print((max(A)//result))
