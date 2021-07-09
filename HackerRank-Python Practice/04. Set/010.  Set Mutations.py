# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
a = set(map(int, input().split()))
N = int(input())
for i in range(N):
    str_ = input().split()
    cmd = str_[0]
    b = set(map(int, input().split()))
    if(cmd == "update"):
        a.update(b)
    elif(cmd == "intersection_update"):
        a.intersection_update(b)
    elif(cmd == "difference_update"):
        a.difference_update(b)
    elif(cmd == "symmetric_difference_update"):
        a.symmetric_difference_update(b)
print(sum(a))
