#SAMPLE INPUT : baab

s = input()
result = []
for i in range(len(s)):
    if ((len(result) == 0) or (result[-1] != s[i])):
        result.append(s[i])
    else :
        result.pop()
        
#how this will work:                SAMPLE INPUT CHARACTER
# loop 1 : result = ['b']                 b
# loop 2 : result = ['b','a']             a
# loop 3 : result = ['b']                 a
# loop 4 : result = []                    b
        
if(len(result) == 0):
    print("Empty String")
else:
    print(''.join(result))
