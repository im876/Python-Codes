n = int(input())
list1 = [1,n]
for i in range(2,n):
    if(n%i==0):
        list1.append(i)
        list1.sort()
        
print(*list1)
