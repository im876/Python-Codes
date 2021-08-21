#Syntax for reading space seperated integers
l1=list(map(int,input("Enter array1").split()))
l2=list(map(int,input("Enter array2").split()))
#Sort in ascending order
l1.sort()
#Sort in descending order
l2.sort(reverse=True)
s=0
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if(i==j):
            s+=(l1[i]*l2[j])
print("Minimum scalar product of two arrays is",end=" ")
print(s)
