# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set_a = set(map(int, input().split()))
n = int(input())
set_b = set(map(int, input().split()))

print(len(set_a.union(set_b)))