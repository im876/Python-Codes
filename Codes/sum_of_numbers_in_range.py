def Sum(n,m):
    result = 0
    for i in range(n,m+1):
        result = result + i
    return result

n,m= map(int, input().split())
print(Sum(n,m))
