#user inputs
Number = int(input('Enter range of number :'))
Divisor = int(input('Enter exact number of divisors :'))
#count1 is to count total number of Numbers with exact divisor
count1 = 0
#driver loop
for i in range(1,Number+1):
    #count2 checks the total number of divisors
    count2 = 0
    #loop to find number of divisors
    for j in range(1,i+1):
        if i % j == 0:
            count2+=1
        else:
            pass
    if count2 == Divisor:
        count1+=1
        #end = " " is used so it can print Numbers in same line
        print(i,end = " ")
#for break in line between Numbers and total count
print('')
print(count1)
