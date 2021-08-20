n = int(input())
temp = n
sum1 = 0

#to store factorial of 0-9
f = [0]*10
f[0] = 1
f[1] = 1
for i in range(2,10):
    f[i] = f[i-1] * i

#to extract digit and add that digits factorial to sum
while(n!=0):
    r = n%10
    n = n // 10
    sum1 += f[r]
    
#check for strong number
if(sum1 == temp):
    print("strong number")
else:
    print("not a strong number")
