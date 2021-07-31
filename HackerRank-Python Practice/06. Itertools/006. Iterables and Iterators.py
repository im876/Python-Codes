# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s = int(input().strip())

list1 = list(input().split(' '))

k = int(input().strip())

c = 0

for i in combinations(list1,k):
    if 'a' in i:
        c += 1

print(c/len(list(combinations(list1,k))))
