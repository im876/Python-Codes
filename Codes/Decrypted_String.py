#Question: Nth character in decrypted string

#Every character in the input string is followed by it's frequency. 
#Write a function to decrypt the string and find the nth character of the decrypted string. 
#If character exists at that position then return "-1"
#For eg:- if the input string is "a2b3" the decrypted string is "aabbb"

#SAMPLE:
#Input1 : a1b1c3
#Input2 : 5
#Output1 : abccc
#Output2 : c

s = input()
n = int(input())
s = list(s)
#print(s)
result = []
for i in range(len(s)):
    if(s[i].isdigit() == True):
        for j in range(int(s[i])):
            result.append(s[i-1])

print("".join(result))
print(result[n-1])
