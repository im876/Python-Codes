'''
Problem Statement
Ninja wanted to go to a party along with his friends. However, his mom wanted him to go only if he completes a task assigned by her.
She gave Ninja a value and asked him to print an X-shaped pattern.
Example : Pattern for N = 3 (No. of rows = 5, No. of columns = 5) :
1   1
 2 2
  3
 2 2
1   1
Since Ninja is in a hurry and doesn’t want to be late for the party; he asks you to solve the problem. Can you help solve this problem?
Input Format:
The first line of input contains an integer ‘T’ denoting the number of test cases. The test cases follow.

The first line of each test case contains a single integer ‘N’.
Output Format:
For each test case, print every row in a new line (row elements not separated by space)

Print the output of each test case in a separate line.
Note:
You are not required to print the expected output; it has already been taken care of. Just implement the function.
Constraints:
1 <= T <= 50
1 <= N <= 1000

Time Limit: 1 sec
Sample Input 1:
2
3
2
Sample Output 1:
1   1
 2 2
  3
 2 2
1   1

 1 1
  2
 1 1
Explanation For Sample Input 1:
In the first test case, ‘N’ is 3, so print the rows from 1 to ‘ 2*N -1 ’, and if the conditions are followed correctly, the above pattern is printed for N=3.

In the second test case, the value of ‘N’ is 2, so print the rows from 1 to ‘2*N - 1’, and if the conditions are followed correctly, the above pattern is printed for N=2.
Sample Input 2:
2
4
5
Sample Output 2:
1     1
 2   2 
  3 3  
   4   
  3 3  
 2   2 
1     1

1       1
 2     2 
  3   3  
   4 4   
    5    
   4 4   
  3   3  
 2     2 
1       1

'''

'''
    Time Complexity: O(N^2)
    Space Complexity: O(1)

    Where 'N' is the number given.
'''


def ninjaPattern(n):

    # Varaibles declared
    value = 1

    # We are running two for loops. The outer one for each row and the inner one for each column.
    for i in range(2 * (n - 1) + 1):
        for j in range(2 * (n - 1) + 1):

            # Check if current row count is equal to current column count. Or if (current column count + row count) is (size - 1).
            if (i == j or (i + j) == 2 * (n - 1)):
                print(value, end = "", sep = '')

            else:
                print(" ", end = "", sep = '')

        # For the remaining values
        if (i < n - 1):
            value += 1

        else:
            value -= 1

        print()


n = int(input())
print(ninjaPattern(n))
