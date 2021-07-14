n = int(input().strip())
p = int(input().strip())

l = p//2
if(n%2 == 0):
    n += 1
else:
    n = n
    
r = (n-p)//2

print(min(l,r))
