def inch_to_feet(n, list1):
    result = 0
    for i in range(n):
        result += list1[i]//12
    return result

n = int(input())
list1 = list(map(int, input().split()))
print(inch_to_feet(n, list1))

#Sample Input 1: 5
#Sample Input 2: 18 11 27 12 14
#Sample Output : 5
