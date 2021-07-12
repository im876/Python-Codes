s,t = map(int, input().split())
a,b = map(int, input().split())
m,n = map(int, input().split())
apple = list(map(int, input().split()))
orange = list(map(int, input().split()))

apple_count = 0
orange_count = 0

for i in range(len(apple)):
    if(s <= a + apple[i] <= t):
        apple_count += 1

for i in range(len(orange)):
    if(s <= b + orange[i] <= t):
        orange_count += 1
        
print(apple_count)
print(orange_count)
