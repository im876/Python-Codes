#Fanny is given a string along with the string which contains single character x. 
#She has to remove the character x from the given string. 
#Help her write a function to remove all occurrences of x character from the given string.


#Input Specification:
#input1: input string s 
#input2: String containing any character x


#Output Specification: String without the occurrence of character x


#Example 1:
#input1: welcome to mettl 
#input2: l
#Output: wecome to mett


a = input("Enter a string:")
r_item = input("Enter the character to remove:")
mylist = list(a)


#remove the item for all its occurrences
for item in mylist:
    if(item==r_item):
        mylist.remove(r_item)

print("".join(mylist))
