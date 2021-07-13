n = int(input())
score = list(map(int, input().rstrip().split()))
min_score = max_score = score[0]
min_count = max_count = 0
for i in score:
    if (i > max_score):
        max_score = i
        max_count += 1
    elif (i < min_score):
        min_score = i
        min_count += 1
        
print(max_count, min_count)
