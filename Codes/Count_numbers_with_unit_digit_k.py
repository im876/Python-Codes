#count numbers with unit digit k
#input a start and end range
#then input a digit

#calculate number of digits wherein the unit digit is present

#Sample Test Case:
#start range , end range = 1 , 45
#Digit to be tested for = 2
#Output = 5 (because numbers with 2 at unit digit place within the range are 2,12,22,32,42 which adds up to == 5 numbers)


def count_numbers(start, end,k):
    count = 0
    for i in range(start, end+1):
        if(i%10 == k):
            count += 1
    return count

start , end = map(int, input().split())
k = int(input())
#print(start)
#print(end)
print(count_numbers(start,end,k))
