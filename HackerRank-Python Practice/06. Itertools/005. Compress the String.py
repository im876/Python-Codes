# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = input().strip()

for i,j in groupby(map(int,list(s))):
    print(tuple([len(list(j)), i]) ,end = " ")
