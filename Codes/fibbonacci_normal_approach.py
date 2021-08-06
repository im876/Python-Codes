def fibbonacci(n):
    if n <= 1:
        return n
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

n = int(input())
result = fibbonacci(n)
print(result)
