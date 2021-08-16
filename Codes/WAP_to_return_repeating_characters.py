## initializing string
string = input()
temp = string.replace(" ", "")
## initializing a list to append all the duplicate characters
duplicates = []
for char in temp:
    ## checking whether the character have a duplicate or not
    ## str.count(char) returns the frequency of a char in the str
    if string.count(char) > 1:
    ## appending to the list if it's already not present
        if char not in duplicates:
            duplicates.append(char)
#print("".join(duplicates))
print(*duplicates)



#Sample Input : Ishan Sandip Modi
#Sample Output : i s a n d
