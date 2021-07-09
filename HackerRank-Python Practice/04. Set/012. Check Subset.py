# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    n_seta = int(input())
    set_a = set(map(int, input().split()))
    n_setb = int(input())
    set_b = set(map(int, input().split()))
    print(set_a.issubset(set_b))
