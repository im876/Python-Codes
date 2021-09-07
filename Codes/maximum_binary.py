'''
A digital machine generates binary data which consists of a string of 0s and 1s. A maximum signal M, in the data, consists of the maximum number of either 1s or 0s appearing consecutively in the data but M can’t be at the beginning or end of the string. Design a way to find the length of the maximum signal.



Input

The first line of the input consists of an integer N, representing the length of the binary string. The second line consists of a string of length N consisting of 0s and 1s only.



Output

Print an integer representing the length of the maximum signal.



Example

Example 1:



Input

6

101000



Output

 1



Explanation

 For 101000, M can be 0 at the second index or at the third index so in both cases max length = 1.  



Example2:



Input

 9

 101111110



Output

 6



Explanation

 For 101111110, M = 111111 so maxlength = 6.



Solution



Input

5

10110

Output

2
'''

size=int(input())
max=0
count=0
flag=0
str=input()
arr=list(str)

for i in range(0,size):
    if arr[i]=='1':
        count=count+1;
        flag=1;
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)
