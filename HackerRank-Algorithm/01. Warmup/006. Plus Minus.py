n = int(input())
arr = list(map(int, input().rstrip().split()))
positive = negative = zeroes = 0
for i in arr:
    if(i > 0):
        positive += 1
    elif(i < 0):
        negative += 1
    elif(i == 0):
        zeroes += 1

print("{:.6f}".format(positive/n))
print("{:.6f}".format(negative/n))
print("{:.6f}".format(zeroes/n))
