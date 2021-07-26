flag = True
n = int(input().strip())
for i in range(1, n+1):
    if(n == i*i):
        flag = True
        break;
    else:
        flag = False
if(flag == True):
    print("Perfect Square")
elif(flag == False):
    print("Not Perfect Square")
