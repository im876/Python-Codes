#function to calculate maximum scalar value
def maxScalar(arr1,arr2, n):
    sumVariable=0
    for i in range(0,n):
        sumVariable+=arr1[i]*arr2[i]
    return sumVariable

#inputs
n=int(input("Enter the size of Array: "))
print("Enter the elements of First Array")
arr1=list(map(int,input().split()))
print("Enter the elements of Second Array")
arr2=list(map(int,input().split()))

#sort arrays in ascending order
arr1.sort()
arr2.sort()

#print maximum scalar value of two arrays
print("Maximum scalar product of two vectors :", maxScalar(arr1,arr2,n))
