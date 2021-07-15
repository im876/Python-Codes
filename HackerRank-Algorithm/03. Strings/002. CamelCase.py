s = input().strip()
count = 1  #since first word is all in lower case hence without count = 1 it won't be counted
for char in s:
    if(char.isupper()):
        count += 1

print(count)

#another approach would be to initialize count as zero and add count by 1 in final print statement
