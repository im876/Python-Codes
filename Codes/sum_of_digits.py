def Sum(n):
    result = 0
    while(n>0):
        result = result + (n%10)
        n = n//10
    return result

n = int(input("Enter a number:"))
print(Sum(n))
