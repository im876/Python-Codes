#program to find whether the given number is an Armstrong number or not using command line arguments.

# An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. 
#For example, 371 is an Armstrong number
#since 3**3 + 7**3 + 1**3 = 371.

num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:
    digit = temp % 10  
    sum += digit ** 3  
    temp //= 10  
    print("digit:", digit)
    print("temp:", temp)
  
if (num == sum):
    print(num,"is an Armstrong number")  
else:  
    print(num,"is not an Armstrong number")  
