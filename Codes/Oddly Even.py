n = input()
odd = 0
even = 0
for i in range(1,len(n)+1):
    if(i%2 == 0):
        even += i
    else:
        odd += i
print(abs(even-odd))

#Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits.

#Input 1 : 4567
#Expected output :2

#Explanation
#The Sum of odd position digits 4 and 6 is 10. The Sum of even position digits 5 and 7 is 12. The difference is 12-10=2.
