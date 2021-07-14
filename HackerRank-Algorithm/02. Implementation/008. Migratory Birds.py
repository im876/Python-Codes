n = int(input())
list1 = list(map(int, input().rstrip().split()))
cnt = [0] * n
for i in list1:
    cnt[i] += 1

#print(cnt)
print(cnt.index(max(cnt)))
