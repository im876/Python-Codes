#Program to check whether a given number is a strong number or not.
def my_factorial(n):
  b=1
  for i in range(1,n+1):
    b=b*i
  return b
  
a=input("Ener a number : ")
sum=0
for i in range(0,len(a)):
  sum=sum+my_factorial(int(a[i]))
print("Sum of factorial of digits : ",sum)
if int(a)==sum:
  print('This is a strong number : ', a)
else:
  print('This is not a strong number', a)
  
  
