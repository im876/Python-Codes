n = int(input()) #no of elements in set
s = set(map(int, input().split())) #set
m = int(input()) #no of commands

for i in range(m):
    string = input().split()
    if string[0] == 'pop':
        s.pop()
    elif string[0] == 'remove':
        s.remove(int(string[1]))
    elif string[0] == 'discard':
        s.discard(int(string[1]))
print(sum(s))
