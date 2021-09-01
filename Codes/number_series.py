'''
Ques. Find the 15th term of the series?

0,0,7,6,14,12,21,18, 28
'''

x,y = 0,0
num = int(input("Enter the nth term to be found out:"))
for i in range(1,num+1):
    if(i%2 != 0):
        x += 7
    else:
        y += 6
        
if(num%2!=0):
    print("{} term is {}".format(num, (x-7)))
else:
    print("{} term is {}".format(num, (y-6)))
