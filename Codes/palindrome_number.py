#program to check whether the given number is Palindrome or not using command line arguments.

a = int(input().strip())
list = []
for digit in str(a):
    list.append(digit)
if(list == list[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")
