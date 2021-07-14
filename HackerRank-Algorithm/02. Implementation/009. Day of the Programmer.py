year = int(input().strip())

#5 test case applicable:
#case 1: year == 1918
#case 2: year == julian but not leap year
#case 3: year == julian and leap year
#case 4: year == gregorian but not leap year
#case 5: year == gregorian and leap year

#case1:
if(year == 1918):
    #print("Transition Year")
    print("26.09.1918")
#case2 and 3:
if(1700 <= year <= 1917):
    if(year % 4 == 0):
        #print("Julian Leap Year") #case3
        print("12.09.%s" %year)
    else:
        #print("Julian Non Leap Year") #case2
        print("13.09.%s" %year)
#case4 and 5:
if(1919 <= year <= 2700):
    if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        #print("Gregorian Leap Year") #case3
        print("12.09.%s" %year)
    else:
        #print("Gregorian Non Leap Year") #case2
        print("13.09.%s" %year)
