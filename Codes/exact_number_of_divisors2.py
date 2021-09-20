'''
Enter the range of number: 30
Enter the exact number of divisors: 3
4 9 25 
3
'''

n = int(input("Enter the range of number: "))
d = int(input("Enter the exact number of divisors: "))
count1 = 0
for i in range(1,n+1):
    count2 = 0
    for j in range(1,i+1):
        if(i%j == 0):
            count2 += 1
        else:
            pass
    if(count2 == d):
        count1 += 1
        print(i, end = " ")
print('')
print(count1)
