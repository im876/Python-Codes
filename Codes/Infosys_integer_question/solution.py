from itertools import permutations
list1 = list(map(int, input().strip().split())) #input from user
permu = permutations(list1,3) #finds all possible combinations

set1 = set(permu) #Makes set of all unique values
max1 = max(set1) #finds the max combination from the set

print("Possible Combinations:")
print(set1) #prints all possible combinations
print(max1) #prints maximum combination

string_ints = [str(int) for int in max1] #converts the max1 into a string list
result = "".join(string_ints)
print(result) #joins the string list into a single stirng
print(len(set1)) #prints length of unique possible combinations

print(result+""+str(len(set1)))
