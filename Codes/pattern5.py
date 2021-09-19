num = int(input("Enter the number:"))

for i in range(1, num+1):
    print(" "*(i-1),end="")
    print("*"*num, end="")
    print()

 '''
 Enter the number:5
*****
 *****
  *****
   *****
    *****
'''
