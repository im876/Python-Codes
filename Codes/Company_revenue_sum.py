#A company has a sales record of N product for M days. 
#The company wishes to know the maximum revenue received from a given product of the N product each day

#Write an algorithm to find the highest revenue received each day

#Input:
#The first line consist of two space separated integer - day(M) and product (N) representing the days 
#and the product in the sales record
#The next M line consist on N space separated integer representing the sales revenue received
#from each product each day

#Output
#Print M space-separated integers representing the maximum revenue received each day

#SAMPLE:
#Input : 
#3 4
#100 198 333 323
#122 232 221 111
#223 565 245 764

#Output :
#333 232 764

n , m = map(int, input().split())
ans = []
for i in range(0,n):
    a = list(map(int, input().split()))
    print(a)
    ans.append(max(a))
    
print(*ans)
