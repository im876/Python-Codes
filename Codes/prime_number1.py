#program that will find the sum of all prime numbers in a given range. 
#The range will be specified as command line parameters. 
#The first command line parameter, N1 which is a positive integer, will contain the lower bound of the range. 
#The second command line parameter N2, which is also a positive integer will contain the upper bound of the range. 
#The program should consider all the prime numbers within the range, excluding the upper bound and lower bound. 
#Print the output in integer format to stdout. 
#Other than the integer number, no other extra information should be printed to stdout. 
#Example Given inputs “7” and “24” here N1= 7 and N2=24, expected output as 83.

lower = int(input())
upper = int(input())
#print("Prime numbers between", lower, "and", upper, "are:")

list1 = []

for num in range(lower+1, upper):
   # all prime numbers are greater than 1
   if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            list1.append(num)
result = sum(list1)
print(result)
