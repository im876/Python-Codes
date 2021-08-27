n=int(input())  
for i in range(n):
    for j in range(2*n+1):
        if(j<n-i-1):       
            print(" ",end="")
        else:
            print("*"*(2*i+1),end="")
            break
    print()
