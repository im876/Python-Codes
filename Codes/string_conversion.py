#program to convert the vowels to an uppercase in a given string using command line arguments.
#Example: if the input is tata, then the expected output is tAtA.

a = input()
a_list = list(a)
vowel = ['a','e','i','o','u']
for i in range(len(a)):
    if a_list[i] in vowel:
        a_list[i] = a_list[i].upper()
        
print("".join(a_list))
