'''
We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12 per sq.ft.

Take input as
1. Number of Interior walls
2. Number of Exterior walls
3. Surface Area of each Interior 4. Wall in units of square feet
Surface Area of each Exterior Wall in units of square feet

If a user enters zero  as the number of walls then skip Surface area values as User may don’t  want to paint that wall.

Calculate and display the total cost of painting the property
Example 1:

6
3
12.3
15.2
12.3
15.2
12.3
15.2
10.10
10.10
10.00
Total estimated Cost : 1847.4 INR
'''
interior_walls = int(input())
exterior_walls = int(input())
if interior_walls:
    int_walls = []
    for i in range(interior_walls):
        int_walls.append(float(input()))

if exterior_walls:
    ext_walls = []
    for i in range(exterior_walls):
        ext_walls.append(float(input()))
if exterior_walls < 0 or interior_walls < 0:
    print("Invalid Input")
    exit()
if exterior_walls and interior_walls:
    print("Total estimated Cost : ",(sum(int_walls)*18+sum(ext_walls)*12),"INR")
else:
    if exterior_walls:
        print("Total estimated Cost : ",sum(ext_walls)*12,"INR")
    elif interior_walls:
         print("Total estimated Cost : ",sum(int_walls)*18,"INR")
    else:
        print("Total estimated Cost : 0.0 INR")
