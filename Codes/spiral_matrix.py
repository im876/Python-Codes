'''
Given a 2D array, print it in spiral form. See the following examples.

NOTE:-  Please comment down the code in other languages as well below .

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output: 
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
'''

def spiralOrder(arr):
    ans=[]
    while arr:
        ans+=arr.pop(0)
        arr= (list(zip(*arr)))[::-1]
        #print("ans :",ans)
        #print("arr :",arr)
    return ans
arr=[[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12],[13, 14, 15, 16, 17, 18]]
print(spiralOrder(arr))
