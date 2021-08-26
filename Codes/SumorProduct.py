'''
Problem Statement
You are given a number ‘N’ and a query ‘Q.’ If ‘Q’ is 1, then you have to return the sum of all integers from 1 to ‘N,’ else if ‘Q’ is equal to 2 then you have to return the product of all integers from 1 to ‘N.’ Since the product can be very large, return it modulo 10 ^ 9 + 7.
For example
Given ‘N’ = 4, ‘Q’ = 1. 
Then the answer is 10 because the sum of all integers between 1 and 4 are 1, 2, 3, and 4. Hence 1 + 2 + 3 + 4 is equal to 10.
Input Format:
The first line of input contains an integer ‘T’ denoting the number of test cases.

Next, ‘T’ lines contain two space-separated integers ‘N’, where ‘N’ is the number given and ‘Q’, denoting the type of query.
Output Format :
For each test case, You are supposed to return an integer denoting the sum or product of ‘N’ numbers.
Note:
You are not required to print the expected output; it has already been taken care of. Just implement the function.
Constraints:
1 <= ‘T’ <= 10
1 <= ‘N’ <= 5000
1 <= ‘Q’ <= 2

Time Limit: 1 sec.
Sample Input 1 :
2
4 1 
4 2
Sample Output 1 :
10
24 
Explanation of the Sample Input 1:
In the first test case, the answer is 10 because all integers between 1 and 4 are 1, 2, 3, and 4. Hence 1 + 2 + 3 + 4 is equal to 10.


In the second test case, the answer is 25 because all integers between 1 and 4 are 1, 2, 3, and 4. Hence 1 * 2 * 3 * 4 is equal to 24.
Sample Input 2 :
2
5 1
5 2 
Sample Output 2 :
15
125
'''

'''
    Time Complexity : O(N)
    Space Complexity : O(1)

    Where 'N' is the number given.
'''


def sumOrProduct(n, q):

    answer = 0
    mod = int(1e9) + 7

    if q == 1:

        # Sum of first 'N' numbers is given by
        # 'N' * 'N + 1' / 2.
        answer = (n * (n + 1)) // 2

    else:
        answer = 1
        for i in range(1, n + 1):
            # Modular Arithmatic.
            i %= mod
            answer %= mod
            answer = (((answer * i) % mod) + mod) % mod

    return answer

n, q = map(int, input().split())
print(sumOrProduct(n,q))
