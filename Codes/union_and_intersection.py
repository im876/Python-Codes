def union(a,b):
    temp = a.union(b)
    result = len(temp)
    return result

def intersection(a,b):
    temp = a.intersection(b)
    result = len(temp)
    return result

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = set(a)
b = set(b)

print("Union Count = ",union(a,b))
print("intersection Count = ",intersection(a,b))
