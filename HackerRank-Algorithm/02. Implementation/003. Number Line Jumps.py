x1, v1, x2, v2 = map(int, input().split())
if((v1 > v2) and (x2 - x1) % (v2-v1) == 0):
    print("YES")
else:
    print("NO")
