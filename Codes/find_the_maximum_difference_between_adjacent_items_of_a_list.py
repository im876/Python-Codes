#find the maximum difference between adjacent items of a list


n = int(input())
list1 = list(map(int, input().split()))
result = []
for i in range(n-1):
    result.append(list1[i] - list1[i+1])
    print("Difference between ",list1[i],"and ",list1[i+1],"is ",result[i])
print("Maximum of those differences is: ",max(result))

#sample input1 : 5
#sample input2 : 10 11 7 12 14
#Sample Output:
#Difference between  10 and  11 is  -1
#Difference between  11 and  7 is  4
#Difference between  7 and  12 is  -5
#Difference between  12 and  14 is  -2
#Maximum of those differences is:  4
