'''
Problem Statement
You have given a sorted array 'A' of 'N' integers.
Now, you are given 'Q' queries, and each query consists of a single integer 'X'. Your task is to check whether 'X' is present in array 'A' or not for each query. If 'X' exists in array 'A', you need to print 1 else print 0.
Note :
The given array is sorted in non-decreasing order. 
Input Format:
The first line of the input contains an integer 'T' representing the number of test cases or queries to be processed. Then the 'T' test case follows. 

The first line of each test case contains a single integer 'N' denoting the size of the array 'A'.

The second line of each test case contains 'N' space-separated integers denoting the elements of the array 'A'.

The third line of each test contains a single integer 'Q', denoting the number of queries. 

Then each of the 'Q' lines from the fourth line of each test case contains a single integer 'X', denoting the desired element to be searched.
Output Format:
For each test case, print 'Q' space-separated integers that denote the answer to the given 'Q' queries, i.e., print 1 if the desired value 'X' exists in the array 'A', otherwise print 0.

Print the answer for each test case in a new line.
Note:
You are not required to print anything, it has already been taken care of. Just implement the function.
Constraints:
1 <= T <= 10 
1 <= N <= 10^5    
-10^9 <= A[i] <= 10^9 
1 <= Q <= 10^4
-10^9 <= X <= 10^9

Where 'T' represents the number of test cases, 'N' represents the size of the array, 'A[i]' represents the elements of the array, 'Q' represents the number of queries and, 'X' denotes the number to be searched.
Time limit: 1 sec
Sample Input 1:
1
5
1 3 5 7 8
2
5
2
Sample Output 1:
  1 0
Explanation For Sample Input 1:
For the first test case, the given array A is [1, 3, 5, 7,8].

So the answer for the given first query is 1 as 5 is present in the array.

For the second query answer is 0 as 2 is not present in the array.  
Sample Input 2:
1
6
1 2 2 3 4 10
3
5
7 
2
Sample Output 2:
 0 0 1
Explanation For Sample Input 2:
For the first test case, the given array A is [1, 2, 2, 3, 4, 10].

So the answer for the given first query is 0 as 5 is not present in the array.

For the given second query answer is 0 as 7 is not present in the array.  

For the given third query answer is 1 as 2 is present in the array.
'''
'''
    Time Complexity  : O(Q*logN).
    Space Complexity : O(1).
    Where N is the size of the given array,
    and Q is the number of queries given.
'''

def binarySearch(arr, x):
    
    # Initialize left and right pointers.
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        
        # Calculate mid.  
        mid = left + (right - left) // 2
        
        # If arr[mid] = x then return 1.
        if arr[mid] == x:
            return 1
        
        # If arr[mid] > x then move right pointer towards left.
        # And search x in left half.
        
        if arr[mid] > x:
            right = mid - 1
            
        # If arr[mid] < x then move left pointer towards right.
        # And search x in right half.
        
        else:
            left = mid + 1
            
    # If x is not found then return 0.
    return 0

def searchInSortedArray(arr,n,queries,q):
    
    ans = []
    
    for x in queries:
        ans.append(binarySearch(arr, x))
        
    return ans

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = []
for i in range(q):
    queries.append(int(input()))
    
print(*searchInSortedArray(arr,n,queries,q))
