low=int(input())
up=int(input())
for i in range(low,up+1):
    if(up>=100):
         print("{:03d}".format(i),end=" ")
    elif(up>=10):
        print("{:02d}".format(i),end=" ")
    else:
        print(i,end=" ")
        
        
#Given a pair of positive integers m and n (m < n; 0 < m < 999; 1 < n < = 999), write a program to smartly affix zeroes, while printing the numbers from m to n.

#Example-1
#Input : 5 10
#Expected output : 05 06 07 08 09 10

#Example-2
#Input : 9 100
#Expected output : 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028 029 030 031 032 033 034 035 036 037 038 039 040 041 042 043 044 045 046 047 048 049 050 051 052 053 054 055 056 057 058 059 060 061 062 063 064 065 067 068 069 070 071 072 073 074 075 076 077 078 079 080 081 082 083 084 085 086 087 088 089 090 091 092 093 094 095 096 097 098 099 100

#Example-3
#Input : 1 9
#Expected Output : 1 2 3 4 5 6 7 8 9
