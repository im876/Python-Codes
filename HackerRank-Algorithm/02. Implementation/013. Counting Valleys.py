steps = int(input().strip())
path = input()

count = 0
result = 0

for c in path:
    if(c == 'U'):
        count += 1
    else:
        count -= 1
    
    if(count == 0 and c == 'U'): #this condition works for valley, since to reach sea level the last element has to be uphill or U so whenever count reaches 0 and the last element was U it means it was a valley
        result += 1
        
print(result)
