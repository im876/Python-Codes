string = input()
temp = string.replace(" ","")

unique = []
for char in temp:
    if(temp.count(char) ==1):
        unique.append(char)
        
print("".join(unique))


#SAMPLE INPUT : AABC
#SAMPLE OUTPUT : BC
