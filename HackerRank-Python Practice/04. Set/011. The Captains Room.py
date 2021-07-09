# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input()) 
l1 = list(map(int, input().split()))
a = set()
b = set()

for i in l1:
    if i not in a:
        a.add(i)
        b.add(i)
    else:
        b.discard(i)
result = list(b)
print(result[0])
