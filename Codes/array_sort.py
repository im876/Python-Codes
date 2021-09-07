'''
You are playing an online game. In the game, a list of N numbers is given. The player has to arrange the numbers so that all the odd numbers of the list come after the even numbers. Write an algorithm to arrange the given list such that all the odd numbers of the list come after the even numbers.



Input

The first line of the input consists of an integer num, representing the size of the list(N). The second line of the input consists of N space-separated integers representing the values of the list



Output

Print N space-separated integers such that all the odd numbers of the list come after the even numbers



Example

Sample Input

8

10 98 3 33 12 22 21 11



Sample Output

10 98 12 22 3 33 21 11



Explanation

 All the even numbers are placed before all the odd numbers.



Solution

Input

8

15 16 14 17 18 19 20 11
'''

def list_sort(n):
    l = len(n)
    even = []
    odd = []
    for i in range(l):
        if(n[i]%2 == 0):
            even.append(n[i])
        else:
            odd.append(n[i])
    result = even + odd
    return result

m = int(input())
n = list(map(int,input().split()))
print(list_sort(n))
