def Sum(n):
    result = 0
    for i in range(1,n+1):
        result = result + i
    return result

n = int(input())
print(Sum(n))
