n = int(input())
sum1 = 1
while(n!=0):
    sum1 = sum1 + (n%10)
    n = n//10
if(n%sum1 == 0):
    print("Harshad Number")
else:
    print("Not a harshad Number")
