a = list(map(int, input("Enter the array element: ").strip().split()))
k = int(input("Enter the kth position: "))
a.sort()
temp = a[::-1]
print("The Sorted Array is: ",a)
print("the kth smallest element in the array is ",a[k-1])
print("the kth largest element in the array is ", temp[k-1])
