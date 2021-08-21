size=int(input("ENTER ARRAY SIZE"))

arr=[]

for i in range(size):

    element=int(input())

    arr.append(element)
arr.sort()
print(arr[1])
