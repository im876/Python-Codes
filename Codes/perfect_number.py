def perfect(n):
    sum = 0
    for i in range(1, num):
        if(n%i == 0):
            sum = sum + i
        if(sum == n):
            return "Perfect Number"
    else:
        return "Not a Perfect Number"
    
n = int(input())
print(perfect(n))
