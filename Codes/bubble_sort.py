'''
Write a program to implement a bubble sort algorithm for sorting the elements of an array.



Input Format:

The first line corresponds to the size of an array.

The second line corresponds to the elements.



Output Format:

Print the element in ascending order.



Sample Input:

6

11 15 26 38 9 10 



Sample Output:

9 10 11 15 26 38



Solution:



Input -

6

45 8 15 91 74 5

'''

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


n=int(input())
arr = list(map(int, input().split()))
  
bubbleSort(arr) 

for i in range(len(arr)): 
    print("%d" %arr[i],end=' ')
