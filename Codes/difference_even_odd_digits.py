'''
Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits

Test Cases:
Case 1
Input: 4567
Expected Output: 2
Explanation : Odd positions are 4 and 6 as they are pos: 1 and pos: 3, both have sum 10. Similarly, 5 and 7 are at even positions pos: 2 and pos: 4 with sum 12. Thus, difference is 12 – 10 = 2

Case 2
Input: 5476
Expected Output: 2

Case 3
Input: 9834698765123
Expected Output: 1
'''
num = [int(d) for d in str(input("Enter the number:"))]
even , odd = 0,0
for i in range(len(num)):
    if(i%2 == 0):
        even += num[i]
    else:
        odd += num[i]
print(abs(odd-even))
