a = list(map(int, input().strip().split()))
k = int(input("Enter the number of rotations: "))
print("array before rotation :",*a)
for i in range(k):
    x = a.pop(-1)
    a.insert(0,x)
print("array after rotation :",*a)

'''
1 2 3 4 5 6
Enter the number of rotations: 2
array before rotation : 1 2 3 4 5 6
array after rotation : 5 6 1 2 3 4
'''
