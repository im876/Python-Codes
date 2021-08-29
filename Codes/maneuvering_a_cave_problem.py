'''
The task is to count all the possible paths from top left to bottom right of a m x n matrix with the constraints that from each cell you can either move only to right or down.

Input: 

First line consists of T test cases. First line of every test case consists of N and M, denoting the number of rows and number of columns respectively.
Output: 

Single line output i.e count of all the possible paths from top left to bottom right of a m x n matrix..
Constraints:

1<=T<=100
1<=N<=100
1<=M<=100
'''

def calculate(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return calculate(a - 1, b) + calculate(a, b - 1)

result = []    
test = int(input())

for i in range(test):
    a, b = map(int,input().split())
    result.append(calculate(a, b))
    
for i in result:
    print(i,end=" ")
