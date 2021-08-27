'''
Floyd’s Triangle is a right-angled triangular array made up of natural numbers. It is named after Robert Floyd. 
It starts from 1 and consecutively selects the next greater number of the sequence.

Total numbers in the triangle of n rows: n*(n+1)/2.
'''
#function to print floyd’s triangle

def floydTriangle(n):

    #count variable

    c=0

    #outer loop for each row

    for i in range(1,n+1):

        #inner loop for each elements in a particular row

        for j in range(0,i):

            c+=1

            #print space seperated elements in  each row

            print(c, end=" ")

        #prints new line for new row

        print()

            

#input

n=int(input("Enter the number of rows: "))

#function call

floydTriangle(n)
