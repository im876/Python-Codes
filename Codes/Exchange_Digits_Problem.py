'''
Compute the nearest larger number by interchanging its digits updated.Given 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and 
if not possible print -1.

Input Format
2 numbers a and b, separated by space.
Output Format
A single number greater than b.
If not possible, print -1

Constraints
1 <= a,b <= 10000000

Example 1:

Sample Input:

    459 500

Sample Output:
    549

Example 2:

Sample Input:

    645757 457765

Sample Output:
    465577

 

Algorithm
Step 1:- Start.
Step 2:- From itertools import permutation function.
Step 3:- Take user inputs.
Step 4:- Initialize a flag variable to 0[zero].
Step 5:- Convert number1 to String and then to a list.
Step 6:- Sort the list by using the sorted function.
Step 7:- Initialize a perm variable that stores the permutations of the list.
Step 8:- Iterate through the perm variable by converting it to the list.
Step 9:- Initialize an empty string.
Step 10:- Concatenate all the iterators to a string variable.
Step 11:- Typecast the string variable to an integer to check the next greatest number.
Step 12:- Continue the process until if condition gets the True value.
Step 13:- As the if condition gets the true value, chang the flag variable to 1 and break the loop.
Step 14:- Check the flag whether we got the greatest value or not.
Step 15:- Print the string variable if flag is 1 else print -1.
Step 16:- End.
'''

from itertools import permutations
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

flag = 0

num1 = list(str(num1))
num1.sort()

perm = list(permutations(num1))

for i in perm:
    string = ""
    for j in i:
        string += j
        
    if(int(string)>num2):
        flag = 1
        break
        
if(flag == 1):
    print("Updated First Number is:",string)
else:
    print("-1")
