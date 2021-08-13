def prime(n):
    for i in range(2, n):
        if(n%i == 0):
            return "Not Prime"
            break
    else:
        return "Prime"
        
        
n = int(input())
print(prime(n))
