a = input()
b = input()
c = input()
a_list = list(a)
b_list = list(b)
vowel = ['a','e','i','o','u']
for i in range(len(a)):
    if a_list[i] in vowel:
        a_list[i] = '*'
for i in range(len(b)):
    if b_list[i] not in vowel:
        b_list[i] = "@"
c = c.upper()

print(("".join(a_list))+("".join(b_list))+c)

#The program will recieve 3 English words inputs from STDIN

#These three words will be read one at a time, in three separate line
#The first word should be changed like all vowels should be replaced by *
#The second word should be changed like all consonants should be replaced by @
#The third word should be changed like all char should be converted to upper case
#Then concatenate the three words and print them
#Other than these concatenated word, no other characters/string should or message should be written to STDOUT

#For example if you print how are you then output should be h*wa@eYOU.

#ishan
#sandip
#modi
#*sh*n@a@@i@MODI
